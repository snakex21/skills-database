#!/usr/bin/env python3
"""
MCP Server for Antigravity Skills Index.

Provides tools to search, retrieve, and discover skills from the local
skills_index.json catalog. Loaded once at startup via lifespan management.

Configuration (in order of precedence):
  1. --skills-dir CLI argument
  2. SKILLS_DIR environment variable
  3. Same directory as server.py (default fallback)
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Server setup & configurable paths
# ---------------------------------------------------------------------------


def resolve_skills_dir(cli_args: list[str] | None = None) -> Path:
    """Resolve the skills directory from CLI args, env var, or fallback.

    Priority (highest first):
      1. --skills-dir CLI argument
      2. SKILLS_DIR environment variable
      3. Directory containing this script (__file__)
    """
    # 1) CLI argument: parse manually so we don't interfere with MCP's own args
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--skills-dir", type=str, default=None)
    try:
        parsed, _ = parser.parse_known_args(cli_args if cli_args else None)
    except SystemExit:
        parsed = argparse.Namespace(skills_dir=None)

    if parsed.skills_dir:
        return Path(parsed.skills_dir).resolve()

    # 2) Environment variable
    env_val = os.environ.get("SKILLS_DIR", "").strip()
    if env_val:
        return Path(env_val).resolve()

    # 3) Fallback — same directory as this script
    return Path(__file__).parent.resolve()


def build_paths(skills_dir: Path):
    """Build all path references from the resolved skills directory."""
    index_path = skills_dir / "skills_index.json"
    if not index_path.is_file():
        print(
            f"Error: {index_path} not found. "
            f"Set --skills-dir or SKILLS_DIR to point to the catalog root.",
            file=sys.stderr,
        )
        sys.exit(1)

    return index_path, skills_dir


# Parse args early so paths are ready before any module-level code runs
_cli_args = sys.argv[1:] if len(sys.argv) > 1 else None
_SKILLS_DIR = resolve_skills_dir(_cli_args)
_SKILLS_INDEX_PATH, _BASE_DIR = build_paths(_SKILLS_DIR)

mcp = FastMCP("antigravity_skills_mcp")


# ---------------------------------------------------------------------------
# Load skills catalog at startup (synchronous — fast JSON load)
# ---------------------------------------------------------------------------

def _load_skills_catalog() -> list[dict[str, Any]]:
    """Load and return the full skills index from disk."""
    with open(_SKILLS_INDEX_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


skills_catalog = _load_skills_catalog()


@mcp.resource("catalog://info")
async def catalog_info() -> str:
    """Return metadata about the loaded skills catalog."""
    total = len(skills_catalog)
    categories = sorted({s.get("category", "uncategorized") for s in skills_catalog})
    return (
        f"Skills Catalog\n"
        f"Total skills: {total}\n"
        f"Categories ({len(categories)}): {', '.join(categories[:20])}"
    )


# ---------------------------------------------------------------------------
# Tool 1 — skills_search
# ---------------------------------------------------------------------------


class SkillsSearchInput(BaseModel):
    """Input model for searching the skills catalog."""

    query: str = Field(
        ...,
        description="Search query string. Supports free-text matching against skill names and descriptions.",
        min_length=1,
        max_length=500,
    )
    limit: int = Field(
        default=20,
        description="Maximum number of results to return (1-100).",
        ge=1,
        le=100,
    )


@mcp.tool(name="skills_search", description="Search the skills catalog by query string.")
async def skills_search(params: SkillsSearchInput) -> str:
    """Search the skills catalog by query string.

    Performs case-insensitive matching against skill 'name' and 'description'
    fields. Returns a ranked list of matching skills with metadata.

    Args:
        params (SkillsSearchInput): Validated input parameters containing:
            - query (str): Search query to match against skill names/descriptions
            - limit (int): Maximum results to return, between 1-100

    Returns:
        str: JSON-formatted string with matching skills and metadata.
    """
    q = params.query.lower().strip()
    if not q:
        return "Error: Query cannot be empty."

    matches: list[dict[str, Any]] = []
    for skill in skills_catalog:
        name = (skill.get("name") or "").lower()
        desc = (skill.get("description") or "").lower()
        # Simple relevance scoring: exact word match > substring match
        score = 0
        if q in name:
            score += 10
        if q in desc:
            score += 5
        # Word-level matching for multi-word queries
        words = q.split()
        for w in words:
            if len(w) < 2:
                continue
            if w in name or w in desc:
                score += 1
        if score > 0:
            matches.append((score, skill))

    # Sort by relevance score descending, then alphabetically
    matches.sort(key=lambda x: (-x[0], (x[1].get("name") or "").lower()))
    results = [m[1] for m in matches[: params.limit]]

    output: list[dict[str, Any]] = []
    for s in results:
        output.append(
            {
                "id": s.get("id", ""),
                "name": s.get("name", ""),
                "category": s.get("category", "uncategorized"),
                "description": s.get("description", ""),
                "risk": s.get("risk", "unknown"),
                "source": s.get("source", ""),
            }
        )

    return json.dumps(
        {"total_matches": len(matches), "returned": len(output), "results": output},
        indent=2,
        ensure_ascii=False,
    )


# ---------------------------------------------------------------------------
# Tool 2 — skills_get
# ---------------------------------------------------------------------------


class SkillsGetInput(BaseModel):
    """Input model for retrieving a specific skill."""

    id: str = Field(
        ...,
        description="The unique identifier (id) of the skill to retrieve.",
        min_length=1,
        max_length=200,
    )


@mcp.tool(name="skills_get", description="Retrieve the full SKILL.md content for a specific skill.")
async def skills_get(params: SkillsGetInput) -> str:
    """Retrieve the full SKILL.md content for a specific skill.

    Looks up the skill by its unique 'id' in the catalog, resolves the file
    path from the index entry, and reads the SKILL.md (or README.md as fallback).

    Args:
        params (SkillsGetInput): Validated input parameters containing:
            - id (str): Unique identifier of the skill to retrieve

    Returns:
        str: The full content of the skill's documentation file.
    """
    sid = params.id.strip()
    if not sid:
        return "Error: Skill ID cannot be empty."

    # Find in catalog
    skill_entry = None
    for s in skills_catalog:
        if s.get("id") == sid:
            skill_entry = s
            break

    if skill_entry is None:
        return f"Error: Skill '{sid}' not found in catalog."

    rel_path = skill_entry.get("path", "")
    # Try SKILL.md first, then README.md as fallback
    for fname in ("SKILL.md", "README.md"):
        full_path = _BASE_DIR / rel_path / fname
        if full_path.is_file():
            try:
                content = full_path.read_text(encoding="utf-8")
                return f"--- Skill: {skill_entry.get('name', sid)} ---\n\n{content}"
            except Exception as e:
                return f"Error reading '{fname}': {e}"

    return (
        f"Error: No SKILL.md or README.md found for skill '{sid}' "
        f"(path: {rel_path}). The skill may not contain documentation."
    )


# ---------------------------------------------------------------------------
# Tool 3 — skills_list_categories
# ---------------------------------------------------------------------------


class SkillsListCategoriesInput(BaseModel):
    """No input required for listing categories."""

    pass


@mcp.tool(name="skills_list_categories", description="List all skill categories with the number of skills in each.")
async def skills_list_categories(params: SkillsListCategoriesInput = None) -> str:  # type: ignore[assignment]
    """List all skill categories with the number of skills in each.

    Returns a sorted list of category names and their skill counts.
    Useful for browsing the catalog structure or finding relevant domains.

    Returns:
        str: JSON-formatted string with category names and counts.
    """
    cat_counts: dict[str, int] = {}
    for s in skills_catalog:
        cat = s.get("category", "uncategorized")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    sorted_cats = sorted(cat_counts.items(), key=lambda x: (-x[1], x[0]))

    output: list[dict[str, Any]] = []
    for cat_name, count in sorted_cats:
        output.append({"category": cat_name, "skill_count": count})

    return json.dumps(
        {"total_categories": len(output), "categories": output}, indent=2
    )


# ---------------------------------------------------------------------------
# Tool 4 — skills_suggest_for_task
# ---------------------------------------------------------------------------


class SkillsSuggestInput(BaseModel):
    """Input model for task-based skill suggestions."""

    task: str = Field(
        ...,
        description="Description of the task or project to find relevant skills.",
        min_length=1,
        max_length=2000,
    )


@mcp.tool(name="skills_suggest_for_task", description="Suggest relevant skills based on a task description.")
async def skills_suggest_for_task(params: SkillsSuggestInput) -> str:
    """Suggest relevant skills based on a task description.

    Analyzes the provided task text and matches it against skill names,
    descriptions, and categories using keyword scoring. Returns ranked
    suggestions with relevance scores.

    Args:
        params (SkillsSuggestInput): Validated input parameters containing:
            - task (str): Natural language description of the task or project

    Returns:
        str: JSON-formatted string with ranked skill suggestions and reasoning.
    """
    task_text = params.task.strip().lower()
    if not task_text:
        return "Error: Task description cannot be empty."

    # Build a set of relevant keywords from the task
    stop_words = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been",
        "to", "of", "in", "on", "for", "with", "by", "at", "from",
        "and", "or", "not", "no", "it", "this", "that", "these",
        "those", "i", "you", "we", "they", "my", "your", "his",
        "her", "its", "our", "their", "what", "which", "who", "how",
        "when", "where", "why", "can", "will", "should", "would",
        "do", "does", "did", "have", "has", "had", "but", "if",
    }

    task_words = set(
        w.strip(".,;:!?\"'()[]{}") for w in task_text.split() if len(w) > 2
    ) - stop_words

    suggestions: list[dict[str, Any]] = []

    for skill in skills_catalog:
        name = (skill.get("name") or "").lower()
        desc = (skill.get("description") or "").lower()
        cat = (skill.get("category") or "").lower()

        score = 0
        matched_words: list[str] = []

        # Name matching — highest weight
        for w in task_words:
            if w in name:
                score += 5
                matched_words.append(w)

        # Description matching — medium weight
        for w in task_words:
            if w in desc and w not in matched_words:
                score += 2
                matched_words.append(w)

        # Category matching — bonus weight
        for w in task_words:
            if w == cat or w in cat:
                score += 3
                matched_words.append(f"cat:{w}")

        if score > 0:
            suggestions.append(
                {
                    "score": score,
                    "matched_keywords": matched_words[:10],
                    "skill": {
                        "id": skill.get("id", ""),
                        "name": skill.get("name", ""),
                        "category": skill.get("category", "uncategorized"),
                        "description": (skill.get("description") or "")[:300],
                        "risk": skill.get("risk", "unknown"),
                    },
                }
            )

    # Sort by score descending, then alphabetically
    suggestions.sort(key=lambda x: (-x["score"], x["skill"]["name"]))

    # Take top 15
    top = suggestions[:15]

    output: list[dict[str, Any]] = []
    for s in top:
        output.append(
            {
                "relevance_score": s["score"],
                "matched_keywords": s["matched_keywords"],
                **s["skill"],
            }
        )

    return json.dumps(
        {"task": params.task, "total_suggestions": len(top), "suggestions": output},
        indent=2,
        ensure_ascii=False,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()


def get_help_text():
    """Return help text for the --skills-dir argument."""
    return (
        "Usage:\n"
        "  python server.py [--skills-dir /path/to/skills]\n\n"
        "Environment variables:\n"
        "  SKILLS_DIR   Path to directory containing skills_index.json and skills/\n\n"
        "Examples:\n"
        '  python server.py --skills-dir ./my-skills\n'
        '  export SKILLS_DIR=/opt/skills && python server.py\n'
    )
