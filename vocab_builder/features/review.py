"""Review functionality for previously missed words."""
from typing import Dict, List
from ..utils.store import ensure_file, read_json, default_history
from ..utils.paths import VOCAB_PATH, HISTORY_PATH
from ..utils.io_helpers import ask_int


def run():
    """Main review function."""
    print("\n=== Review Mistakes ===")
    
    wrong_bank = load_wrong_bank()
    
    if not wrong_bank:
        print("No wrong answers to review yet. Take a quiz first!")
        return
    
    # Show available words for review
    print(f"Words available for review: {len(wrong_bank)}")
    for word, count in sorted(wrong_bank.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {word}: missed {count} times")
    
    # Ask how many to review
    max_review = min(5, len(wrong_bank))  # Limit to 5 for beginners
    num_review = ask_int(f"How many words to review? (1-{max_review}): ")
    num_review = min(num_review, max_review)
    
    # Select review set and run review quiz
    vocab = read_json(VOCAB_PATH)
    review_words = select_review_set(wrong_bank, vocab, num_review)
    
    if review_words:
        print(f"\nReviewing {len(review_words)} words...")
        summary = quiz_review_set(review_words)
        print(f"Review complete! Score: {summary['correct']}/{summary['num']}")
    else:
        print("No words selected for review.")


def load_wrong_bank() -> Dict[str, int]:
    """Load wrong answer bank from history.json."""
    ensure_file(HISTORY_PATH, default_history)
    history = read_json(HISTORY_PATH)
    return history.get("wrong_bank", {})


def select_review_set(bank: Dict[str, int], vocab: Dict, limit: int = 5) -> List[Dict]:
    """Select words for review based on miss count."""
    # Sort by miss count (descending) and take top words
    sorted_words = sorted(bank.items(), key=lambda x: x[1], reverse=True)
    
    # Get word entries from vocab
    review_words = []
    vocab_words = {w["word"].lower(): w for w in vocab.get("words", [])}
    
    for word, _ in sorted_words[:limit]:
        if word.lower() in vocab_words:
            review_words.append(vocab_words[word.lower()])
    
    return review_words


def quiz_review_set(words: List[Dict]) -> Dict:
    """Run a simple review quiz on the selected words."""
    outcomes = []
    
    for i, word in enumerate(words, 1):
        print(f"\nReview {i}/{len(words)}: {word['word']}")
        print(f"Meaning: {word['meaning']}")
        
        # Simple review - just ask if they remember
        user_input = input("Do you remember this word? (yes/no): ").strip().lower()
        correct = user_input in ["yes", "y"]
        
        if correct:
            print("Great! You remembered it! ✓")
        else:
            print("Keep practicing this word!")
        
        outcomes.append((word["word"], correct))
        
        # TODO: On correct answers, decrement that word in wrong_bank (min 0) and persist
        # Put your code here
        if correct:
            # Placeholder for decrementing wrong_bank
            pass
    
    # Simple scoring
    num_total = len(outcomes)
    num_correct = sum(1 for _, correct in outcomes if correct)
    
    return {
        "num": num_total,
        "correct": num_correct,
        "wrong": [word for word, correct in outcomes if not correct]
    }
