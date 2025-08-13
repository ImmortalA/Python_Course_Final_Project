"""Add new vocabulary words to the system."""
from datetime import datetime, timezone
from typing import Dict
from ..utils.store import ensure_file, read_json, write_json, default_vocab
from ..utils.paths import VOCAB_PATH
from ..utils.io_helpers import ask_str, ask_choice


def run():
    """Main function to add new words."""
    print("\n=== Add New Word ===")
    
    while True:
        choice = ask_choice("Add a word? (yes/no): ", ["yes", "no"])
        if choice == "no":
            break
            
        word_entry = collect_word()
        if word_entry:
            save_word(word_entry)
            print(f"Added '{word_entry['word']}' successfully!")
        else:
            print("Word addition cancelled.")
    
    print("Returning to main menu...")


def collect_word() -> Dict:
    """Collect word information from user.
    
    TODO: Add simple validation here
    - Check if word is not empty
    - Check if word is not too long (more than 20 letters)
    - Give helpful error message if wrong
    """
    word = ask_str("Enter word: ")
    
    # TODO: Add simple validation here
    # - Check if word is not empty
    # - Check if word is not too long (more than 20 letters)
    # - Give helpful error message if wrong
    # Put your code here
    
    meaning = ask_str("Enter meaning: ")
    # TODO: Add simple validation here too
    # - Check if meaning is not empty
    # - Check if meaning is not too long (more than 100 letters)
    # Put your code here
    
    return {
        "word": word,
        "meaning": meaning,
        "added_at": datetime.now(timezone.utc).isoformat()
    }


def word_exists(vocab: Dict, word: str) -> bool:
    """Check if word already exists (case-insensitive)."""
    return any(entry["word"].lower() == word.lower() for entry in vocab.get("words", []))


def save_word(entry: Dict) -> None:
    """Save word to vocab.json with timestamp."""
    ensure_file(VOCAB_PATH, default_vocab)
    vocab = read_json(VOCAB_PATH)
    
    vocab["words"].append(entry)
    write_json(VOCAB_PATH, vocab)
