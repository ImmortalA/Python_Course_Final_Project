"""Main entry point for Vocabulary Builder application."""
try:
    from .features import add_word, view_words, quiz, review
    from .utils.io_helpers import ask_int
    from .utils.store import ensure_file, default_vocab, default_history
    from .utils.paths import VOCAB_PATH, HISTORY_PATH
except ImportError:
    # For direct execution
    from vocab_builder.features import add_word, view_words, quiz, review
    from vocab_builder.utils.io_helpers import ask_int
    from vocab_builder.utils.store import ensure_file, default_vocab, default_history
    from vocab_builder.utils.paths import VOCAB_PATH, HISTORY_PATH


def show_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("           Vocabulary Builder")
    print("="*50)
    print("1) Add a new word")
    print("2) View words")
    print("3) Quiz me (randomized)")
    print("4) Review mistakes")
    print("0) Exit")
    print("="*50)


def main():
    """Main application loop."""
    # Ensure data files exist on first run
    ensure_file(VOCAB_PATH, default_vocab)
    ensure_file(HISTORY_PATH, default_history)
    
    print("Welcome to Vocabulary Builder!")
    print("Your personal vocabulary learning assistant.")
    
    # Main menu loop
    while True:
        show_menu()
        
        try:
            choice = ask_int("Enter your choice (0-4): ")
            
            if choice == 0:
                print("Goodbye! Keep building your vocabulary!")
                break
            elif choice == 1:
                add_word.run()
            elif choice == 2:
                view_words.run()
            elif choice == 3:
                quiz.run()
            elif choice == 4:
                review.run()
            else:
                print("Invalid choice. Please enter 0-4.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye! Keep building your vocabulary!")
            break
        except Exception as e:
            # TODO: Improve error messages (Step 2)
            # Put your code here
            print(f"An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
