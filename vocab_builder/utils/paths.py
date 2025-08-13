"""Path utilities for the Vocabulary Builder application."""
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Data directory and file paths
DATA_DIR = PROJECT_ROOT / "vocab_builder" / "data"
VOCAB_PATH = DATA_DIR / "vocab.json"
HISTORY_PATH = DATA_DIR / "history.json"
