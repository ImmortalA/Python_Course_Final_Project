"""Quiz functionality for vocabulary testing."""
import random
from datetime import datetime, timezone
from typing import Dict, List, Tuple
from ..utils.store import ensure_file, read_json, write_json, default_vocab, default_history
from ..utils.paths import VOCAB_PATH, HISTORY_PATH
from ..utils.io_helpers import ask_int, ask_choice


def run(mode: str = "mcq"):
    """Main quiz function."""
    print("\n=== Take a Quiz ===")
    
    words = load_words()
    if len(words) < 2:
        print("You need at least 2 words to take a quiz. Add more words first!")
        return
    
    # Ask how many questions
    max_questions = min(10, len(words))
    num_questions = ask_int(f"How many questions? (1-{max_questions}): ")
    num_questions = min(num_questions, max_questions)
    
    print(f"\nStarting quiz with {num_questions} questions...")
    print()
    
    outcomes = []
    
    # Select random words for quiz
    quiz_words = random.sample(words, num_questions)
    
    for i, word in enumerate(quiz_words, 1):
        print(f"Question {i}/{num_questions}")
        
        if mode == "mcq":
            correct = ask_mcq(word)
        else:
            correct = ask_typing(word)
        
        outcomes.append((word["word"], correct))
        print()
    
    # Score the session
    summary = score_session(outcomes)
    print(f"Quiz complete! Score: {summary['correct']}/{summary['num']}")
    
    # Record the session
    record_session(summary)


def load_words() -> List[Dict]:
    """Load words from vocab.json."""
    ensure_file(VOCAB_PATH, default_vocab)
    vocab = read_json(VOCAB_PATH)
    return vocab.get("words", [])


def ask_mcq(word: Dict) -> bool:
    """Ask a multiple choice question."""
    print(f"What does '{word['word']}' mean?")
    
    # TODO: Make this simpler
    # - Pick one random word
    # - Show the word and ask "What does this mean?"
    # - Give 2 choices: correct meaning + 1 wrong meaning
    # Put your code here
    
    # Simple 2-choice question for now
    choices = [word["meaning"], "Wrong answer"]
    random.shuffle(choices)
    
    print("1) " + choices[0])
    print("2) " + choices[1])
    
    user_answer = ask_int("Your answer (1 or 2): ")
    
    if user_answer == 1 and choices[0] == word["meaning"]:
        print("Correct! ✓")
        return True
    elif user_answer == 2 and choices[1] == word["meaning"]:
        print("Correct! ✓")
        return True
    else:
        print(f"Wrong! The correct answer is: {word['meaning']}")
        return False


def ask_typing(word: Dict) -> bool:
    """Ask user to type the meaning."""
    print(f"What does '{word['word']}' mean?")
    user_answer = input("Your answer: ").strip().lower()
    correct_meaning = word['meaning'].lower()
    
    if user_answer == correct_meaning:
        print("Correct! ✓")
        return True
    else:
        print(f"Wrong! The correct answer is: {word['meaning']}")
        return False


def score_session(outcomes: List[Tuple[str, bool]]) -> Dict:
    """Score the quiz session and return summary."""
    num_total = len(outcomes)
    num_correct = sum(1 for _, correct in outcomes if correct)
    wrong_words = [word for word, correct in outcomes if not correct]
    
    return {
        "num": num_total,
        "correct": num_correct,
        "wrong": wrong_words
    }


def record_session(summary: Dict) -> None:
    """Record quiz session in history.json."""
    ensure_file(HISTORY_PATH, default_history)
    history = read_json(HISTORY_PATH)
    
    # Add session record
    session_record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "score": summary["correct"],
        "total": summary["num"],
        "wrong_words": summary["wrong"]
    }
    history["sessions"].append(session_record)
    
    # Update wrong answer bank
    for word in summary["wrong"]:
        if word in history["wrong_bank"]:
            history["wrong_bank"][word] += 1
        else:
            history["wrong_bank"][word] = 1
    
    write_json(HISTORY_PATH, history)
