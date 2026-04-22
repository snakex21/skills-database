# Skills Database MCP Server

---

## 🇬🇧 English

A Python MCP (Model Context Protocol) server that provides tools to search, retrieve, and discover skills from a local `skills_index.json` catalog. Designed for integration with AI coding assistants such as [OpenCode](https://github.com/opencode), Claude, Codex, and others.

### Features

- **Search** — Find skills by name or description with relevance scoring
- **Retrieve** — Get the full `SKILL.md` content for any skill in the catalog
- **Browse categories** — List all available skill categories with counts
- **Task suggestions** — Get AI-relevant skill recommendations based on a task description

### Installation

```bash
git clone https://github.com/<your-username>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# or:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Configuration

The server resolves the skills directory using one of three methods (in order of precedence):

| Priority | Method | Example |
|----------|--------|---------|
| 1️⃣ | CLI argument `--skills-dir` | `python server.py --skills-dir /path/to/skills` |
| 2️⃣ | Environment variable `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Default fallback | Same directory as `server.py` |

### Usage

```bash
# Default — uses same directory as server.py
python server.py

# Custom skills directory via CLI
python server.py --skills-dir /path/to/your/skills/root

# With environment variable (Linux/macOS)
export SKILLS_DIR=/path/to/your/skills/root
python server.py

# With environment variable (Windows PowerShell)
$env:SKILLS_DIR = "/path/to/your/skills/root"
python server.py
```

### Integration with OpenCode

Add to your OpenCode configuration (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolute/path/to/skills-database"
    }
  }
}
```

### Available Tools

| Tool | Description |
|------|-------------|
| `skills_search` | Search skills by query string with relevance scoring |
| `skills_get` | Retrieve full SKILL.md content for a specific skill by ID |
| `skills_list_categories` | List all categories and their skill counts |
| `skills_suggest_for_task` | Get skill recommendations based on a task description |

### Available Resource

| Resource | Description |
|----------|-------------|
| `catalog://info` | Returns metadata about the loaded skills catalog (total count, categories) |

---

## 🇵🇱 Polski

Pythonowy serwer MCP (Model Context Protocol), który udostępnia narzędzia do wyszukiwania, pobierania i odkrywania umiejętności z lokalnego katalogu `skills_index.json`. Zaprojektowany do integracji z asystentami programistycznymi AI takimi jak [OpenCode](https://github.com/opencode), Claude, Codex i inni.

### Funkcje

- **Wyszukiwanie** — Wyszukuj umiejętności po nazwie lub opisie z oceną trafności
- **Pobieranie** — Pobierz pełną zawartość `SKILL.md` dla dowolnej umiejętności w katalogu
- **Przeglądaj kategorie** — Wyświetl wszystkie dostępne kategorie umiejętności z liczbami
- **Sugestie zadań** — Otrzymuj rekomendacje umiejętności AI na podstawie opisu zadania

### Instalacja

```bash
git clone https://github.com/<twoja-nazwa>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# lub:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Konfiguracja

Serwer resolve'uje katalog umiejętności za pomocą jednej z trzech metod (w kolejności priorytetów):

| Priorytet | Metoda | Przykład |
|-----------|--------|----------|
| 1️⃣ | Argument CLI `--skills-dir` | `python server.py --skills-dir /sciezka/do/skills` |
| 2️⃣ | Zmienna środowiskowa `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Domyślne fallback | Ten sam katalog co `server.py` |

### Uruchomienie

```bash
# Domyślnie — używa tego samego katalogu co server.py
python server.py

# Własny katalog umiejętności przez CLI
python server.py --skills-dir /sciezka/do/katalogu/skills

# Ze zmienną środowiskową (Linux/macOS)
export SKILLS_DIR=/sciezka/do/katalogu/skills
python server.py

# Ze zmienną środowiskową (Windows PowerShell)
$env:SKILLS_DIR = "/sciezka/do/katalogu/skills"
python server.py
```

### Integracja z OpenCode

Dodaj do konfiguracji OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolutna/sciezka/do/skills-database"
    }
  }
}
```

### Dostępne narzędzia

| Narzędzie | Opis |
|-----------|------|
| `skills_search` | Wyszukaj umiejętności po zapytaniu z oceną trafności |
| `skills_get` | Pobierz pełną zawartość SKILL.md dla konkretnej umiejętności po ID |
| `skills_list_categories` | Wyświetl wszystkie kategorie i ich liczbę umiejętności |
| `skills_suggest_for_task` | Otrzymaj rekomendacje umiejętności na podstawie opisu zadania |

### Dostępny zasób

| Zasób | Opis |
|-------|------|
| `catalog://info` | Zwraca metadane załadowanego katalogu umiejętności (liczba całkowita, kategorie) |

---

## 🇩🇪 Deutsch

Ein Python MCP-Server (Model Context Protocol), der Tools zum Suchen, Abrufen und Entdecken von Fähigkeiten aus einem lokalen `skills_index.json`-Katalog bereitstellt. Entwickelt für die Integration mit KI-Coding-Assistants wie [OpenCode](https://github.com/opencode), Claude, Codex und anderen.

### Funktionen

- **Suche** — Finde Fähigkeiten nach Name oder Beschreibung mit Relevanzbewertung
- **Abrufen** — Hole den vollständigen `SKILL.md`-Inhalt für jede Fähigkeit im Katalog
- **Kategorien durchsuchen** — Liste alle verfügbaren Fähigkeitskategorien mit Zählern
- **Aufgabenvorschläge** — Erhalte KI-relevante Fähigkeitsempfehlungen basierend auf einer Aufgabenbeschreibung

### Installation

```bash
git clone https://github.com/<dein-nutzername>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# oder:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Konfiguration

Der Server löst das Fähigkeiten-Verzeichnis mit einer von drei Methoden (in Prioritätsreihenfolge):

| Priorität | Methode | Beispiel |
|-----------|---------|----------|
| 1️⃣ | CLI-Argument `--skills-dir` | `python server.py --skills-dir /pfad/zu/skills` |
| 2️⃣ | Umgebungsvariable `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Standard-Fallback | Gleiches Verzeichnis wie `server.py` |

### Verwendung

```bash
# Standard — verwendet das gleiche Verzeichnis wie server.py
python server.py

# Benutzerdefiniertes Fähigkeiten-Verzeichnis über CLI
python server.py --skills-dir /pfad/zu/deinem/skills/root

# Mit Umgebungsvariable (Linux/macOS)
export SKILLS_DIR=/pfad/zu/deinem/skills/root
python server.py

# Mit Umgebungsvariable (Windows PowerShell)
$env:SKILLS_DIR = "/pfad/zu/deinem/skills/root"
python server.py
```

### Integration mit OpenCode

Füge dies deiner OpenCode-Konfiguration (`~/.config/opencode/config.json`) hinzu:

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absoluter/pfad/zu/skills-database"
    }
  }
}
```

### Verfügbare Tools

| Tool | Beschreibung |
|------|-------------|
| `skills_search` | Fähigkeiten nach Suchstring mit Relevanzbewertung durchsuchen |
| `skills_get` | Vollständigen SKILL.md-Inhalt für eine bestimmte Fähigkeit nach ID abrufen |
| `skills_list_categories` | Alle Kategorien und ihre Fähigkeitsanzahl auflisten |
| `skills_suggest_for_task` | Fähigkeitsempfehlungen basierend auf einer Aufgabenbeschreibung erhalten |

### Verfügbare Ressource

| Ressource | Beschreibung |
|-----------|-------------|
| `catalog://info` | Gibt Metadaten über den geladenen Fähigkeitenkatalog zurück (Gesamtzahl, Kategorien) |

---

## 🇪🇸 Español

Un servidor MCP (Model Context Protocol) en Python que proporciona herramientas para buscar, recuperar y descubrir habilidades desde un catálogo local `skills_index.json`. Diseñado para la integración con asistentes de codificación por IA como [OpenCode](https://github.com/opencode), Claude, Codex y otros.

### Características

- **Búsqueda** — Encuentra habilidades por nombre o descripción con puntuación de relevancia
- **Recuperar** — Obtén el contenido completo de `SKILL.md` para cualquier habilidad en el catálogo
- **Explorar categorías** — Lista todas las categorías de habilidades disponibles con sus conteos
- **Sugerencias de tareas** — Obtiene recomendaciones de habilidades relevantes para IA basadas en una descripción de tarea

### Instalación

```bash
git clone https://github.com/<tu-usuario>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# o:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Configuración

El servidor resuelve el directorio de habilidades usando uno de tres métodos (en orden de precedencia):

| Prioridad | Método | Ejemplo |
|-----------|--------|---------|
| 1️⃣ | Argumento CLI `--skills-dir` | `python server.py --skills-dir /ruta/a/skills` |
| 2️⃣ | Variable de entorno `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Fallback por defecto | Mismo directorio que `server.py` |

### Uso

```bash
# Por defecto — usa el mismo directorio que server.py
python server.py

# Directorio de habilidades personalizado vía CLI
python server.py --skills-dir /ruta/a/tu/skills/root

# Con variable de entorno (Linux/macOS)
export SKILLS_DIR=/ruta/a/tu/skills/root
python server.py

# Con variable de entorno (Windows PowerShell)
$env:SKILLS_DIR = "/ruta/a/tu/skills/root"
python server.py
```

### Integración con OpenCode

Añade a tu configuración de OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/ruta/absoluta/a/skills-database"
    }
  }
}
```

### Herramientas disponibles

| Herramienta | Descripción |
|-------------|-------------|
| `skills_search` | Buscar habilidades por cadena de consulta con puntuación de relevancia |
| `skills_get` | Recuperar contenido completo SKILL.md para una habilidad específica por ID |
| `skills_list_categories` | Listar todas las categorías y sus conteos de habilidades |
| `skills_suggest_for_task` | Obtener recomendaciones de habilidades basadas en una descripción de tarea |

### Recurso disponible

| Recurso | Descripción |
|---------|-------------|
| `catalog://info` | Devuelve metadatos sobre el catálogo de habilidades cargado (conteo total, categorías) |

---

## 🇨🇳 中文

一个 Python MCP（Model Context Protocol）服务器，提供从本地 `skills_index.json` 目录中搜索、检索和发现技能的工具。专为与 AI 编程助手如 [OpenCode](https://github.com/opencode)、Claude、Codex 等集成而设计。

### 功能特性

- **搜索** — 通过名称或描述搜索技能，并带有相关性评分
- **检索** — 获取目录中任何技能的完整 `SKILL.md` 内容
- **浏览分类** — 列出所有可用的技能分类及其数量
- **任务建议** — 根据任务描述获取 AI 相关的技能推荐

### 安装

```bash
git clone https://github.com/<你的用户名>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# 或:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### 配置

服务器使用以下三种方法之一解析技能目录（按优先级顺序）：

| 优先级 | 方法 | 示例 |
|--------|------|------|
| 1️⃣ | CLI 参数 `--skills-dir` | `python server.py --skills-dir /path/to/skills` |
| 2️⃣ | 环境变量 `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | 默认回退 | 与 `server.py` 相同的目录 |

### 使用方法

```bash
# 默认 — 使用与 server.py 相同的目录
python server.py

# 通过 CLI 指定自定义技能目录
python server.py --skills-dir /path/to/your/skills/root

# 使用环境变量（Linux/macOS）
export SKILLS_DIR=/path/to/your/skills/root
python server.py

# 使用环境变量（Windows PowerShell）
$env:SKILLS_DIR = "/path/to/your/skills/root"
python server.py
```

### 与 OpenCode 集成

添加到你的 OpenCode 配置 (`~/.config/opencode/config.json`)：

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolute/path/to/skills-database"
    }
  }
}
```

### 可用工具

| 工具 | 描述 |
|------|------|
| `skills_search` | 通过查询字符串搜索技能并带有相关性评分 |
| `skills_get` | 根据 ID 检索特定技能的完整 SKILL.md 内容 |
| `skills_list_categories` | 列出所有分类及其技能数量 |
| `skills_suggest_for_task` | 根据任务描述获取技能推荐 |

### 可用资源

| 资源 | 描述 |
|------|------|
| `catalog://info` | 返回已加载技能目录的元数据（总数、分类） |

---

## 🇫🇷 Français

Un serveur MCP (Model Context Protocol) en Python qui fournit des outils pour rechercher, récupérer et découvrir des compétences depuis un catalogue local `skills_index.json`. Conçu pour l'intégration avec des assistants de codage IA tels que [OpenCode](https://github.com/opencode), Claude, Codex et d'autres.

### Fonctionnalités

- **Recherche** — Trouvez des compétences par nom ou description avec scoring de pertinence
- **Récupération** — Obtenez le contenu complet `SKILL.md` pour toute compétence du catalogue
- **Parcourir les catégories** — Liste toutes les catégories de compétences disponibles avec leurs comptes
- **Suggestions de tâches** — Recevez des recommandations de compétences pertinentes pour l'IA basées sur une description de tâche

### Installation

```bash
git clone https://github.com/<votre-nom>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# ou :
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Configuration

Le serveur résout le répertoire de compétences en utilisant l'une des trois méthodes (par ordre de priorité) :

| Priorité | Méthode | Exemple |
|----------|---------|---------|
| 1️⃣ | Argument CLI `--skills-dir` | `python server.py --skills-dir /chemin/vers/skills` |
| 2️⃣ | Variable d'environnement `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Repli par défaut | Même répertoire que `server.py` |

### Utilisation

```bash
# Par défaut — utilise le même répertoire que server.py
python server.py

# Répertoire de compétences personnalisé via CLI
python server.py --skills-dir /chemin/vers/votre/skills/root

# Avec variable d'environnement (Linux/macOS)
export SKILLS_DIR=/chemin/vers/votre/skills/root
python server.py

# Avec variable d'environnement (Windows PowerShell)
$env:SKILLS_DIR = "/chemin/vers/votre/skills/root"
python server.py
```

### Intégration avec OpenCode

Ajoutez à votre configuration OpenCode (`~/.config/opencode/config.json`) :

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/chemin/absolu/vers/skills-database"
    }
  }
}
```

### Outils disponibles

| Outil | Description |
|-------|-------------|
| `skills_search` | Rechercher des compétences par chaîne de requête avec scoring de pertinence |
| `skills_get` | Récupérer le contenu SKILL.md complet pour une compétence spécifique par ID |
| `skills_list_categories` | Lister toutes les catégories et leurs comptes de compétences |
| `skills_suggest_for_task` | Obtenir des recommandations de compétences basées sur une description de tâche |

### Ressource disponible

| Ressource | Description |
|-----------|-------------|
| `catalog://info` | Retourne les métadonnées du catalogue de compétences chargé (nombre total, catégories) |

---

## 🇫🇮 Suomi

Python MCP -palvelin (Model Context Protocol), joka tarjoaa työkaluja paikallisen `skills_index.json`-katalogin taitojen etsimiseen, noutamiseen ja löytämiseen. Suunniteltu integroitavaksi tekoälyohjelmointiavustajiin kuten [OpenCode](https://github.com/opencode), Claude, Codex ja muut.

### Ominaisuudet

- **Haku** — Etsi taitoja nimen tai kuvauksen perusteella merkityksellisyyden pisteytyksellä
- **Nouto** — Hae koko `SKILL.md`-sisältö mille tahansa taidolle katalogissa
- **Selaa kategorioita** — Lista kaikki saatavilla olevat taitokategoriat lukuineen
- **Tehtäväehdotukset** — Saat AI:n kannalta merkityksellisiä taitosuositustehtävän kuvauksen perusteella

### Asennus

```bash
git clone https://github.com/<kayttajanimi>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# tai:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Määritys

Palvelu ratkaisee taitohakemiston käyttäen yhtä kolmesta menetelmästä (tärkeysjärjestyksessä):

| Tärkeys | Menetelmä | Esimerkki |
|---------|-----------|-----------|
| 1️⃣ | CLI-argumentti `--skills-dir` | `python server.py --skills-dir /polku/taidot` |
| 2️⃣ | Ympäristömuuttuja `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Oletusvarajärjestelmä | Sama hakemisto kuin `server.py` |

### Käyttö

```bash
# Oletus — käyttää samaa hakemistoa kuin server.py
python server.py

# Mukautettu taitohakemisto CLI:n kautta
python server.py --skills-dir /polku/taidot/root

# Ympäristömuuttujalla (Linux/macOS)
export SKILLS_DIR=/polku/taidot/root
python server.py

# Ympäristömuuttujalla (Windows PowerShell)
$env:SKILLS_DIR = "/polku/taidot/root"
python server.py
```

### Integrointi OpenCoden kanssa

Lisää OpenCode-konfiguraatioosi (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absoluuttinen/polku/skills-database"
    }
  }
}
```

### Saatavilla olevat työkalut

| Työkalu | Kuvaus |
|---------|--------|
| `skills_search` | Etsi taitoja kyselymerkkijonolla merkityksellisyyden pisteytyksellä |
| `skills_get` | Nouda koko SKILL.md-sisältö tietylle taidolle ID:n perusteella |
| `skills_list_categories` | Lista kaikki kategoriat ja niiden taitomäärät |
| `skills_suggest_for_task` | Saat taitosuositukset tehtävän kuvauksen perusteella |

### Saatavilla oleva resurssi

| Resurssi | Kuvaus |
|----------|--------|
| `catalog://info` | Palauttaa ladatun taitokatalogin metatiedot (kokonaismäärä, kategoriat) |

---

## 🇨🇿 Čeština

Pythonový MCP server (Model Context Protocol), který poskytuje nástroje pro vyhledávání, získávání a objevování dovedností z místního katalogu `skills_index.json`. Navrženo pro integraci s AI asistenty pro programování jako [OpenCode](https://github.com/opencode), Claude, Codex a další.

### Funkce

- **Vyhledávání** — Najděte dovednosti podle jména nebo popisu s hodnocením relevance
- **Získání** — Získejte plný obsah `SKILL.md` pro jakoukoli dovednost v katalogu
- **Procházení kategorií** — Seznam všech dostupných kategorií dovedností s počty
- **Doporučení úloh** — Získejte doporučení dovedností relevantních pro AI na základě popisu úlohy

### Instalace

```bash
git clone https://github.com/<vas-jmeno>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# nebo:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Konfigurace

Server určuje adresář dovedností pomocí jedné ze tří metod (v pořadí priorit):

| Priorita | Metoda | Příklad |
|----------|--------|---------|
| 1️⃣ | CLI argument `--skills-dir` | `python server.py --skills-dir /cesta/k/skills` |
| 2️⃣ | Proměnná prostředí `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Výchozí záloha | Stejný adresář jako `server.py` |

### Použití

```bash
# Výchozí — používá stejný adresář jako server.py
python server.py

# Vlastní adresář dovedností přes CLI
python server.py --skills-dir /cesta/k/vam/skills/root

# S proměnnou prostředí (Linux/macOS)
export SKILLS_DIR=/cesta/k/vam/skills/root
python server.py

# S proměnnou prostředí (Windows PowerShell)
$env:SKILLS_DIR = "/cesta/k/vam/skills/root"
python server.py
```

### Integrace s OpenCode

Přidejte do konfigurace OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolutni/cesta/k/skills-database"
    }
  }
}
```

### Dostupné nástroje

| Nástroj | Popis |
|---------|-------|
| `skills_search` | Vyhledávání dovedností podle řetězce dotazu s hodnocením relevance |
| `skills_get` | Získání plného obsahu SKILL.md pro konkrétní dovednost podle ID |
| `skills_list_categories` | Výpis všech kategorií a jejich počtů dovedností |
| `skills_suggest_for_task` | Získání doporučení dovedností na základě popisu úlohy |

### Dostupný zdroj

| Zdroj | Popis |
|-------|-------|
| `catalog://info` | Vrátí metadata o načteném katalogu dovedností (celkový počet, kategorie) |

---

## 🇸🇰 Slovenčina

Pythonový MCP server (Model Context Protocol), ktorý poskytuje nástroje na vyhľadávanie, získavanie a objavovanie zručností z lokálneho katalógu `skills_index.json`. Navrhnutý pre integráciu s AI asistentmi pre programovanie ako [OpenCode](https://github.com/opencode), Claude, Codex a ďalšie.

### Funkcie

- **Vyhľadávanie** — Nájdite zručnosti podľa mena alebo popisu s hodnotením relevance
- **Získanie** — Získajte plný obsah `SKILL.md` pre ľubovoľnú zručnosť v katalógu
- **Prehliadanie kategórií** — Zoznam všetkých dostupných kategórií zručností s počtami
- **Odporúčania úloh** — Získajte odporúčania zručností relevantných pre AI na základe popisu úlohy

### Inštalácia

```bash
git clone https://github.com/<vas-meno>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# alebo:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Konfigurácia

Server určuje adresár zručností pomocou jednej zo troch metód (v poradí priorít):

| Priorita | Metóda | Príklad |
|----------|--------|---------|
| 1️⃣ | CLI argument `--skills-dir` | `python server.py --skills-dir /cesta/k/skills` |
| 2️⃣ | Premenná prostredia `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Predvolená záloha | Rovnaký adresár ako `server.py` |

### Použitie

```bash
# Predvolené — používa rovnaký adresár ako server.py
python server.py

# Vlastný adresár zručností cez CLI
python server.py --skills-dir /cesta/k/vam/skills/root

# S premennou prostredia (Linux/macOS)
export SKILLS_DIR=/cesta/k/vam/skills/root
python server.py

# S premennou prostredia (Windows PowerShell)
$env:SKILLS_DIR = "/cesta/k/vam/skills/root"
python server.py
```

### Integrácia s OpenCode

Pridajte do konfigurácie OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolutna/cesta/k/skills-database"
    }
  }
}
```

### Dostupné nástroje

| Nástroj | Popis |
|---------|-------|
| `skills_search` | Vyhľadávanie zručností podľa reťazca dotazu s hodnotením relevance |
| `skills_get` | Získanie plného obsahu SKILL.md pre konkrétnu zručnosť podľa ID |
| `skills_list_categories` | Výpis všetkých kategórií a ich počtov zručností |
| `skills_suggest_for_task` | Získanie odporúčaní zručností na základe popisu úlohy |

### Dostupný zdroj

| Zdroj | Popis |
|-------|-------|
| `catalog://info` | Vrátia metadáta o načtenom katalógu zručností (celkový počet, kategórie) |

---

## 🇷🇺 Русский

Python MCP-сервер (Model Context Protocol), предоставляющий инструменты для поиска, получения и обнаружения навыков из локального каталога `skills_index.json`. Предназначен для интеграции с AI-ассистентами для программирования, такими как [OpenCode](https://github.com/opencode), Claude, Codex и другие.

### Возможности

- **Поиск** — Найдите навыки по имени или описанию с оценкой релевантности
- **Получение** — Получите полное содержимое `SKILL.md` для любого навыка в каталоге
- **Просмотр категорий** — Список всех доступных категорий навыков с количеством
- **Рекомендации задач** — Получите рекомендации навыков, релевантных для ИИ, на основе описания задачи

### Установка

```bash
git clone https://github.com/<ваше-имя>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# или:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Конфигурация

Сервер определяет каталог навыков с помощью одного из трёх методов (в порядке приоритета):

| Приоритет | Метод | Пример |
|-----------|-------|--------|
| 1️⃣ | Аргумент CLI `--skills-dir` | `python server.py --skills-dir /путь/к/skills` |
| 2️⃣ | Переменная окружения `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Резервный вариант по умолчанию | Тот же каталог, что и `server.py` |

### Использование

```bash
# По умолчанию — использует тот же каталог, что и server.py
python server.py

# Пользовательский каталог навыков через CLI
python server.py --skills-dir /путь/к/вашим/skills/root

# С переменной окружения (Linux/macOS)
export SKILLS_DIR=/путь/к/вашим/skills/root
python server.py

# С переменной окружения (Windows PowerShell)
$env:SKILLS_DIR = "/путь/к/вашим/skills/root"
python server.py
```

### Интеграция с OpenCode

Добавьте в конфигурацию OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/абсолютный/путь/к/skills-database"
    }
  }
}
```

### Доступные инструменты

| Инструмент | Описание |
|------------|----------|
| `skills_search` | Поиск навыков по строке запроса с оценкой релевантности |
| `skills_get` | Получение полного содержимого SKILL.md для конкретного навыка по ID |
| `skills_list_categories` | Список всех категорий и их количества навыков |
| `skills_suggest_for_task` | Получение рекомендаций навыков на основе описания задачи |

### Доступный ресурс

| Ресурс | Описание |
|--------|----------|
| `catalog://info` | Возвращает метаданные загруженного каталога навыков (общее количество, категории) |

---

## 🇧🇾 Беларуская

Python MCP-сервер (Model Context Protocol), які забяспечвае інструменты для пошуку, атрымання і выяўлення навыкаў з лакальнага каталога `skills_index.json`. Прызначаны для інтэграцыі з AI-асістэнтамі для праграмавання, такімі як [OpenCode](https://github.com/opencode), Claude, Codex і іншыя.

### Магчымасці

- **Пошук** — Знайдзіце навыкі па імені або апісанні з ацэнкай рэлевантнасці
- **Атрыманне** — Атрымайце поўнае змесціва `SKILL.md` для любога навыку ў каталозе
- **Прагляд катэгорый** — Спіс усіх даступных катэгорый навыкаў з колькасцю
- **Рэкамендацыі задач** — Атрымайце рэкамендацыі навыкаў, рэлевантных для ШІ, на аснове апісання задачы

### Усталёўка

```bash
git clone https://github.com/<ваше-імя>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# або:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Канфігурацыя

Сервер вызначае каталог навыкаў з дапамогай аднаго з трох метадаў (у парадку прыярытэту):

| Прыярытэт | Метод | Прыклад |
|-----------|-------|---------|
| 1️⃣ | Аргумент CLI `--skills-dir` | `python server.py --skills-dir /шлях/да/skills` |
| 2️⃣ | Зменная асяроддзя `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Рэзервовы варыянт па змаўчанні | Той жа каталог, што і `server.py` |

### Выкарыстанне

```bash
# Па змаўчанні — выкарыстоўвае той жа каталог, што і server.py
python server.py

| Карыстацкі каталог навыкаў праз CLI
python server.py --skills-dir /шлях/да/вашым/skills/root

# З зменнай асяроддзя (Linux/macOS)
export SKILLS_DIR=/шлях/да/вашым/skills/root
python server.py

# З зменнай асяроддзя (Windows PowerShell)
$env:SKILLS_DIR = "/шлях/да/вашым/skills/root"
python server.py
```

### Інтэграцыя з OpenCode

Дадайце ў канфігурацыю OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/абсалютны/шлях/да/skills-database"
    }
  }
}
```

### Даступныя інструменты

| Інструмент | Апісанне |
|------------|----------|
| `skills_search` | Пошук навыкаў па радку запыту з ацэнкай рэлевантнасці |
| `skills_get` | Атрыманне поўнага змесціва SKILL.md для канкрэтнага навыку па ID |
| `skills_list_categories` | Спіс усіх катэгорый і іх колькасці навыкаў |
| `skills_suggest_for_task` | Атрыманне рэкамендацый навыкаў на аснове апісання задачы |

### Даступны рэсурс

| Рэсурс | Апісанне |
|--------|----------|
| `catalog://info` | Вяртае метаданыя загружанага каталога навыкаў (агульная колькасць, катэгорыі) |

---

## 🇺🇦 Українська

Python MCP-сервер (Model Context Protocol), який забезпечує інструменти для пошуку, отримання та виявлення навичок з локального каталогу `skills_index.json`. Призначений для інтеграції з AI-асистентами для програмування, такими як [OpenCode](https://github.com/opencode), Claude, Codex та інші.

### Можливості

- **Пошук** — Знайдіть навички за іменем або описом з оцінкою релевантності
- **Отримання** — Отримайте повний вміст `SKILL.md` для будь-якої навички в каталозі
- **Перегляд категорій** — Список усіх доступних категорій навичок з кількістю
- **Рекомендації задач** — Отримайте рекомендації навичок, релевантних для ШІ, на основі опису задачі

### Встановлення

```bash
git clone https://github.com/<ваше-ім'я>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# або:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Конфігурація

Сервер визначає каталог навичок за допомогою одного з трьох методів (у порядку пріоритету):

| Пріоритет | Метод | Приклад |
|-----------|-------|---------|
| 1️⃣ | Аргумент CLI `--skills-dir` | `python server.py --skills-dir /шлях/до/skills` |
| 2️⃣ | Змінна середовища `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Резервний варіант за замовчуванням | Той самий каталог, що й `server.py` |

### Використання

```bash
# За замовчуванням — використовує той самий каталог, що й server.py
python server.py

# Користувацький каталог навичок через CLI
python server.py --skills-dir /шлях/до/вашим/skills/root

# З змінною середовища (Linux/macOS)
export SKILLS_DIR=/шлях/до/вашим/skills/root
python server.py

# З змінною середовища (Windows PowerShell)
$env:SKILLS_DIR = "/шлях/до/вашим/skills/root"
python server.py
```

### Інтеграція з OpenCode

Додайте до конфігурації OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/абсолютний/шлях/до/skills-database"
    }
  }
}
```

### Доступні інструменти

| Інструмент | Опис |
|------------|------|
| `skills_search` | Пошук навичок за рядком запиту з оцінкою релевантності |
| `skills_get` | Отримання повного вмісту SKILL.md для конкретної навички за ID |
| `skills_list_categories` | Список усіх категорій та їх кількості навичок |
| `skills_suggest_for_task` | Отримання рекомендацій навичок на основі опису задачі |

### Доступний ресурс

| Ресурс | Опис |
|--------|------|
| `catalog://info` | Повертає метадані завантаженого каталогу навичок (загальна кількість, категорії) |

---

## 🇳🇴 Norsk

En Python MCP-server (Model Context Protocol) som tilbyr verktøy for å søke, hente og oppdage ferdigheter fra en lokal `skills_index.json`-katalog. Designet for integrasjon med AI-kodingsassistenter som [OpenCode](https://github.com/opencode), Claude, Codex og andre.

### Funksjoner

- **Søk** — Finn ferdigheter etter navn eller beskrivelse med relevansvurdering
- **Hent** — Hent fullt `SKILL.md`-innhold for hvilken som helst ferdighet i katalogen
- **Bla gjennom kategorier** — Liste over alle tilgjengelige ferdighetskategorier med tellinger
- **Oppgaveforslag** — Få AI-relevante ferdighetsanbefalinger basert på en oppgavebeskrivelse

### Installasjon

```bash
git clone https://github.com/<ditt-brukernavn>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# eller:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Konfigurasjon

Serveren løser ferdighetsmappen ved å bruke en av tre metoder (i prioriteringsrekkefølge):

| Prioritet | Metode | Eksempel |
|-----------|--------|----------|
| 1️⃣ | CLI-argument `--skills-dir` | `python server.py --skills-dir /sti/til/skills` |
| 2️⃣ | Miljøvariabel `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Standard fallback | Samme mappe som `server.py` |

### Bruk

```bash
# Standard — bruker samme mappe som server.py
python server.py

# Tilpasset ferdighetsmappe via CLI
python server.py --skills-dir /sti/til/din/skills/root

# Med miljøvariabel (Linux/macOS)
export SKILLS_DIR=/sti/til/din/skills/root
python server.py

# Med miljøvariabel (Windows PowerShell)
$env:SKILLS_DIR = "/sti/til/din/skills/root"
python server.py
```

### Integrering med OpenCode

Legg til i din OpenCode-konfigurasjon (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolutt/sti/til/skills-database"
    }
  }
}
```

### Tilgjengelige verktøy

| Verktøy | Beskrivelse |
|---------|-------------|
| `skills_search` | Søk etter ferdigheter med søkestreng og relevansvurdering |
| `skills_get` | Hent fullt SKILL.md-innhold for en bestemt ferdighet per ID |
| `skills_list_categories` | Liste over alle kategorier og deres ferdighetsantall |
| `skills_suggest_for_task` | Få ferdighetsanbefalinger basert på en oppgavebeskrivelse |

### Tilgjengelig ressurs

| Ressurs | Beskrivelse |
|---------|-------------|
| `catalog://info` | Returnerer metadata om den lastede ferdighetskatalogen (totalt antall, kategorier) |

---

## 🇸🇪 Svenska

En Python MCP-server (Model Context Protocol) som tillhandahåller verktyg för att söka, hämta och upptäcka färdigheter från en lokal `skills_index.json`-katalog. Designad för integration med AI-kodningsassistenter som [OpenCode](https://github.com/opencode), Claude, Codex och andra.

### Funktioner

- **Sök** — Hitta färdigheter efter namn eller beskrivning med relevansbedömning
- **Hämta** — Hämta fullt `SKILL.md`-innehåll för vilken färdighet som helst i katalogen
- **Bläddra kategorier** — Lista över alla tillgängliga färdighetskategorier med räkningar
- **Uppgiftsförslag** — Få AI-relevanta färdighetsrekommendationer baserat på en uppgiftsbeskrivning

### Installation

```bash
git clone https://github.com/<ditt-anvandarnamn>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# eller:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Konfiguration

Servern löser färdighetsmappen med en av tre metoder (i prioriteringsordning):

| Prioritet | Metod | Exempel |
|-----------|-------|---------|
| 1️⃣ | CLI-argument `--skills-dir` | `python server.py --skills-dir /sankt/till/skills` |
| 2️⃣ | Miljövärdering `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Standard fallback | Samma mapp som `server.py` |

### Användning

```bash
# Standard — använder samma mapp som server.py
python server.py

# Anpassad färdighetsmapp via CLI
python server.py --skills-dir /sankt/till/din/skills/root

# Med miljövärdering (Linux/macOS)
export SKILLS_DIR=/sankt/till/din/skills/root
python server.py

# Med miljövärdering (Windows PowerShell)
$env:SKILLS_DIR = "/sankt/till/din/skills/root"
python server.py
```

### Integration med OpenCode

Lägg till i din OpenCode-konfiguration (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolut/sankt/till/skills-database"
    }
  }
}
```

### Tillgängliga verktyg

| Verktyg | Beskrivning |
|---------|-------------|
| `skills_search` | Sök efter färdigheter med söksträng och relevansbedömning |
| `skills_get` | Hämta fullt SKILL.md-innehåll för en specifik färdighet per ID |
| `skills_list_categories` | Lista över alla kategorier och deras färdighetsantal |
| `skills_suggest_for_task` | Få färdighetsrekommendationer baserat på en uppgiftsbeskrivning |

### Tillgänglig resurs

| Resurs | Beskrivning |
|--------|-------------|
| `catalog://info` | Returnerar metadata om den lastade färdighetskatalogen (totalt antal, kategorier) |

---

## 🇩🇰 Dansk

En Python MCP-server (Model Context Protocol), der tilbyder værktøjer til at søge, hente og opdage færdigheder fra en lokal `skills_index.json`-katalog. Designet til integration med AI-kodningsassistenter som [OpenCode](https://github.com/opencode), Claude, Codex og andre.

### Funktioner

- **Søg** — Find færdigheder efter navn eller beskrivelse med relevansbedømmelse
- **Hent** — Hent fuld `SKILL.md`-indhold for enhver færdighed i katalogen
- **Gennemse kategorier** — Liste over alle tilgængelige færdigheds kategorier med tællinger
- **Opgaveforslag** — Få AI-relevante færdighedsanbefalinger baseret på en opgavebeskrivelse

### Installation

```bash
git clone https://github.com/<dit-brugernavn>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# eller:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Konfiguration

Serveren løser færdigheds mappen ved at bruge en af tre metoder (i prioriterings rækkefølge):

| Prioritet | Metode | Eksempel |
|-----------|--------|----------|
| 1️⃣ | CLI-argument `--skills-dir` | `python server.py --skills-dir /sti/til/skills` |
| 2️⃣ | Miljøvariabel `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Standard fallback | Samme mappe som `server.py` |

### Brug

```bash
# Standard — bruger samme mappe som server.py
python server.py

# Tilpasset færdighedsmappe via CLI
python server.py --skills-dir /sti/til/din/skills/root

# Med miljøvariabel (Linux/macOS)
export SKILLS_DIR=/sti/til/din/skills/root
python server.py

# Med miljøvariabel (Windows PowerShell)
$env:SKILLS_DIR = "/sti/til/din/skills/root"
python server.py
```

### Integration med OpenCode

Tilføj til din OpenCode-konfiguration (`~/.config/opencode/config.json`):

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolut/sti/til/skills-database"
    }
  }
}
```

### Tilgængelige værktøjer

| Værktøj | Beskrivelse |
|---------|-------------|
| `skills_search` | Søg efter færdigheder med søgestreng og relevansbedømmelse |
| `skills_get` | Hent fuld SKILL.md-indhold for en bestemt færdighed per ID |
| `skills_list_categories` | Liste over alle kategorier og deres færdighedsantal |
| `skills_suggest_for_task` | Få færdighedsanbefalinger baseret på en opgavebeskrivelse |

### Tilgængelig ressource

| Ressource | Beskrivelse |
|-----------|-------------|
| `catalog://info` | Returnerer metadata om den lastede færdigheds katalog (totalt antal, kategorier) |

---

## 🇯🇵 日本語

ローカルの `skills_index.json` カタログからスキルを検索、取得、発見するためのツールを提供する Python MCP（Model Context Protocol）サーバー。[OpenCode](https://github.com/opencode)、Claude、Codex などの AI コーディングアシスタントとの統合のために設計されています。

### 機能

- **検索** — スキルの名前または説明で関連性スコアリング付きで検索
- **取得** — カタログ内の任意のスキルの完全な `SKILL.md` コンテンツを取得
- **カテゴリ閲覧** — 利用可能なすべてのスキルカテゴリとそのカウントをリスト
- **タスク提案** — タスクの説明に基づいて AI 関連のスキル推奨を取得

### インストール

```bash
git clone https://github.com/<あなたのユーザー名>/skills-database.git
cd skills-database
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# または:
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### 設定

サーバーは3つの方法のいずれかを使用してスキルディレクトリを解決します（優先度順）：

| 優先度 | 方法 | 例 |
|--------|------|-----|
| 1️⃣ | CLI引数 `--skills-dir` | `python server.py --skills-dir /path/to/skills` |
| 2️⃣ | 環境変数 `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | デフォルトのフォールバック | `server.py` と同じディレクトリ |

### 使用方法

```bash
# デフォルト — server.py と同じディレクトリを使用
python server.py

# CLI経由でカスタムスキルディレクトリを指定
python server.py --skills-dir /path/to/your/skills/root

# 環境変数を使用（Linux/macOS）
export SKILLS_DIR=/path/to/your/skills/root
python server.py

# 環境変数を使用（Windows PowerShell）
$env:SKILLS_DIR = "/path/to/your/skills/root"
python server.py
```

### OpenCode との統合

OpenCode 設定 (`~/.config/opencode/config.json`) に追加：

```json
{
  "mcpServers": {
    "skills_database": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolute/path/to/skills-database"
    }
  }
}
```

### 利用可能なツール

| ツール | 説明 |
|--------|------|
| `skills_search` | クエリ文字列で関連性スコアリング付きスキルを検索 |
| `skills_get` | ID で特定のスキルの完全な SKILL.md コンテンツを取得 |
| `skills_list_categories` | すべてのカテゴリとそのスキル数をリスト |
| `skills_suggest_for_task` | タスクの説明に基づいてスキル推奨を取得 |

### 利用可能なリソース

| リソース | 説明 |
|----------|------|
| `catalog://info` | ロードされたスキルカタログのメタデータ（総数、カテゴリ）を返す |
