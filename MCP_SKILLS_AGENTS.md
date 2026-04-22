# Skills Search MCP Server

## Co to jest

Serwer MCP w Pythonie który wystawia narzędzia do przeszukiwania bazy skills z repozytorium antigravity-awesome-skills. Agent w OpenCode zamiast ładować 1200+ skills do kontekstu, wywołuje konkretne narzędzie i dostaje tylko to czego potrzebuje.

---

## Stack

- **Python 3.11+**
- **FastMCP** (z pakietu `mcp`)
- **Transport**: stdio (lokalne użycie)
- **Instalacja**: `pip install mcp`

---

## Struktura projektu

```
C:\Programy\MCP\skills-mcp\
├── server.py          # jedyny plik — cały serwer MCP
└── requirements.txt   # mcp>=1.0.0
```

Serwer czyta dane z:
```
C:\Programy\MCP\antigravity-awesome-skills-main\skills_index.json
C:\Programy\MCP\antigravity-awesome-skills-main\skills\
```

---

## Stałe na początku server.py

```python
SKILLS_INDEX_PATH = r"C:\Programy\MCP\antigravity-awesome-skills-main\skills_index.json"
SKILLS_DIR = r"C:\Programy\MCP\antigravity-awesome-skills-main\skills"
MAX_RESULTS = 5
MAX_SKILL_CONTENT_CHARS = 8000
```

---

## Ładowanie indeksu

Załaduj `skills_index.json` raz przy starcie serwera przez lifespan:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def app_lifespan():
    index = load_skills_index()  # wczytaj JSON do pamięci
    yield {"index": index}

mcp = FastMCP("skills_mcp", lifespan=app_lifespan)
```

Funkcja `load_skills_index()` — wczytuje JSON, zwraca listę dictów.

---

## 4 narzędzia

### 1. `skills_search`

Szuka skills po query. Przeszukuje pola `name`, `description`, `category` każdego skilla.

**Input:**
```python
class SearchInput(BaseModel):
    query: str = Field(..., description="Słowa kluczowe, np. 'python architecture' lub 'security audit'", min_length=1, max_length=200)
    category: Optional[str] = Field(default=None, description="Filtruj po kategorii, np. 'security', 'testing', 'architecture'")
    limit: int = Field(default=5, description="Maksymalna liczba wyników", ge=1, le=10)
```

**Logika wyszukiwania:**
- Rozbij query na słowa
- Dla każdego skilla policz ile słów query pasuje do `name` + `description` + `category` (case-insensitive)
- Sortuj po liczbie trafień malejąco
- Zwróć top `limit` wyników

**Output** (markdown):
```
## Search results for "python architecture"

### 1. python-patterns
**Category**: development
**Description**: Python design patterns, best practices...
**Path**: skills/python-patterns

### 2. architecture
**Category**: architecture  
**Description**: System design, ADRs...
**Path**: skills/architecture
```

**Annotations:**
```python
annotations={
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False
}
```

---

### 2. `skills_get`

Zwraca pełną treść konkretnego SKILL.md.

**Input:**
```python
class GetInput(BaseModel):
    skill_id: str = Field(..., description="ID skilla z wyników search, np. 'python-patterns' lub 'architecture'", min_length=1, max_length=100)
```

**Logika:**
- Znajdź skill po `id` w załadowanym indeksie
- Zbuduj ścieżkę: `SKILLS_DIR / skill_path / SKILL.md`
- Wczytaj plik, przytnij do `MAX_SKILL_CONTENT_CHARS` jeśli za długi
- Zwróć treść z nagłówkiem

**Output:**
```
## SKILL: python-patterns
**Category**: development | **Risk**: safe

[pełna treść SKILL.md, max 8000 znaków]

---
*Truncated to 8000 chars. Full file: skills/python-patterns/SKILL.md*
```

Jeśli skill nie istnieje:
```
Error: Skill 'xyz' not found. Use skills_search to find available skills.
```

---

### 3. `skills_list_categories`

Zwraca listę wszystkich dostępnych kategorii z liczbą skills w każdej.

**Input:** brak parametrów (pusta klasa BaseModel)

**Logika:**
- Policz skills per kategoria z indeksu
- Sortuj alfabetycznie

**Output:**
```
## Available skill categories (42 categories, 1239 skills)

| Category | Count |
|----------|-------|
| architecture | 45 |
| business | 38 |
| data | 67 |
| development | 120 |
| ...
```

---

### 4. `skills_suggest_for_task`

Wyższy poziom — agent opisuje zadanie, MCP sugeruje kombinację 2-3 skills.

**Input:**
```python
class SuggestInput(BaseModel):
    task: str = Field(..., description="Opis zadania, np. 'chcę zbudować REST API w FastAPI z testami i dokumentacją'", min_length=10, max_length=500)
```

**Logika:**
- Wyciągnij kluczowe słowa z `task`
- Wywołaj wewnętrznie tę samą logikę co `skills_search` dla każdego słowa kluczowego
- Deduplikuj wyniki
- Zwróć max 3 skills z uzasadnieniem dlaczego pasują

**Output:**
```
## Suggested skills for your task

**Task**: "chcę zbudować REST API w FastAPI z testami i dokumentacją"

### Recommended combination:

1. **fastapi-patterns** (development)
   *Why*: Covers FastAPI project structure and best practices
   
2. **test-driven-development** (testing)
   *Why*: TDD patterns for API testing
   
3. **api-design-principles** (architecture)
   *Why*: REST API design guidelines and documentation

**Usage**: Call skills_get with each skill_id to load full content.
```

---

## Konfiguracja w OpenCode (opencode.jsonc)

Po zbudowaniu serwera dodaj do `opencode.jsonc`:

```json
"mcp": {
  "skills-search": {
    "type": "local",
    "command": ["python", "C:/Programy/MCP/skills-mcp/server.py"],
    "enabled": true
  }
}
```

---

## requirements.txt

```
mcp>=1.0.0
```

---

## Obsługa błędów

- Brak `skills_index.json` → jasny komunikat z oczekiwaną ścieżką przy starcie
- Brak pliku `SKILL.md` dla danego skilla → informacja że plik nie istnieje lokalnie
- Puste wyniki search → sugestia żeby spróbować innych słów kluczowych lub `skills_list_categories`

---

## Kolejność implementacji

1. `requirements.txt`
2. Stałe i `load_skills_index()`
3. Lifespan z ładowaniem indeksu
4. `skills_list_categories` (najprostszy — tylko agregacja)
5. `skills_search` (główny tool)
6. `skills_get` (czytanie pliku)
7. `skills_suggest_for_task` (kompozycja)
8. Test: `python server.py` — nie może rzucać błędów przy starcie

