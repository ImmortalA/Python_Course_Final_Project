"""View and display vocabulary words."""
from typing import Dict
from ..utils.store import ensure_file, read_json, default_vocab
from ..utils.paths import VOCAB_PATH


def run():
    """Display all vocabulary words."""
    print("\n=== View All Words ===")
    
    ensure_file(VOCAB_PATH, default_vocab)
    vocab = read_json(VOCAB_PATH)
    words = vocab.get("words", [])
    
    if not words:
        print("No words yet! Add some words first.")
        return
    
    print(f"You have {len(words)} word(s):")
    print()
    
    # TODO: Make this look better
    # - Show each word on a new line
    # - Add some spacing between words
    # - Show "No words yet!" if list is empty
    # Put your code here
    
    for i, word_entry in enumerate(words, 1):
        print(f"{i}. {word_entry['word']}")
        print(f"   Meaning: {word_entry['meaning']}")
        print()
    
    print("End of word list.")
