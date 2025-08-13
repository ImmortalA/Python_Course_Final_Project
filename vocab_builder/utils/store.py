"""Data storage utilities for JSON files."""
import json
from pathlib import Path
from typing import Dict, Any, Callable


def ensure_file(path: Path, default_factory: Callable[[], Dict[str, Any]]) -> None:
    """Ensure a file exists, creating it with default content if missing."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with open(path, 'w') as f:
            json.dump(default_factory(), f, indent=2, ensure_ascii=False)


def read_json(path: Path) -> Dict[str, Any]:
    """Read JSON data from a file.
    
    TODO: Add simple error message (Step 5)
    - If file is broken, show "File is broken, starting fresh"
    - Don't crash the app
    """
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Put your code here
        raise ValueError(f"Error reading {path}. File may be corrupted or missing.")


def write_json(path: Path, data: Dict[str, Any]) -> None:
    """Write data to a JSON file."""
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def default_vocab() -> Dict[str, Any]:
    """Default vocabulary data structure."""
    return {"meta": {"version": 1}, "words": []}


def default_history() -> Dict[str, Any]:
    """Default history data structure."""
    return {"sessions": [], "wrong_bank": {}}
