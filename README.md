# Antigravity Skills MCP Server

A Python MCP (Model Context Protocol) server that provides tools to search, retrieve, and discover skills from a local `skills_index.json` catalog. Designed for integration with AI coding assistants such as [OpenCode](https://github.com/opencode), Claude, Codex, and others.

## Features

- **Search** — Find skills by name or description with relevance scoring
- **Retrieve** — Get the full `SKILL.md` content for any skill in the catalog
- **Browse categories** — List all available skill categories with counts
- **Task suggestions** — Get AI-relevant skill recommendations based on a task description

## Installation

### Prerequisites

- Python 3.10+
- pip (Python package manager)

### Steps

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# or:
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

## Configuration

The server resolves the skills directory using one of three methods (in order of precedence):

| Priority | Method | Example |
|----------|--------|---------|
| 1️⃣ | CLI argument `--skills-dir` | `python server.py --skills-dir /path/to/skills` |
| 2️⃣ | Environment variable `SKILLS_DIR` | `export SKILLS_DIR=/opt/skills` |
| 3️⃣ | Default fallback | Same directory as `server.py` |

### Using a `.env` file

Create a `.env` file in the project root:

```env
SKILLS_DIR=./skills-root
```

> **Note:** The path should point to the directory containing both `skills_index.json` and the `skills/` subdirectory.

### Directory structure expected

```
your-skills-root/
├── skills_index.json      ← JSON catalog of all skills
└── skills/                ← Subfolder with individual skill directories
    ├── angular-best-practices/
    │   └── SKILL.md
    ├── python-testing/
    │   └── SKILL.md
    └── ...
```

## Usage

### Run the server (default — uses same directory as `server.py`)

```bash
python server.py
```

### Run with a custom skills directory via CLI

```bash
python server.py --skills-dir /path/to/your/skills/root
```

### Run with an environment variable

```bash
# Linux / macOS
export SKILLS_DIR=/path/to/your/skills/root
python server.py

# Windows (PowerShell)
$env:SKILLS_DIR = "/path/to/your/skills/root"
python server.py
```

## Integration with OpenCode

To connect this MCP server to **OpenCode**, add the following configuration to your OpenCode settings.

### Option 1 — Inline JSON config

In your OpenCode configuration file (usually `~/.config/opencode/config.json` or similar), add:

```json
{
  "mcpServers": {
    "antigravity_skills": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolute/path/to/this/repo"
    }
  }
}
```

### Option 2 — With custom skills directory

If your `skills_index.json` lives outside the repo:

```json
{
  "mcpServers": {
    "antigravity_skills": {
      "command": "python",
      "args": ["server.py", "--skills-dir", "/path/to/your/skills/root"],
      "cwd": "/absolute/path/to/this/repo"
    }
  }
}
```

### Option 3 — Using SKILLS_DIR environment variable

```json
{
  "mcpServers": {
    "antigravity_skills": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/absolute/path/to/this/repo",
      "env": {
        "SKILLS_DIR": "/path/to/your/skills/root"
      }
    }
  }
}
```

### Available Tools in OpenCode

Once connected, the following tools will be available:

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

## Project Structure

```
.
├── server.py              # MCP server entry point
├── skills_index.json      # Skills catalog index
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore             # Git ignore rules
└── skills/                # Individual skill directories (SKILL.md files)
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
