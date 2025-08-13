"""Input/output helper functions for user interaction."""
from typing import List


def ask_str(prompt: str) -> str:
    """Ask for a string input and re-prompt until non-empty.
    
    TODO: Add simple validation here (Step 2)
    - Check if input is not empty
    - Check if input is not too long
    - Give helpful error message if wrong
    """
    while True:
        user_input = input(prompt).strip()
        # Put your code here
        if user_input:
            return user_input
        print("Please enter a non-empty value.")


def ask_int(prompt: str) -> int:
    """Ask for an integer input and re-prompt until valid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def ask_choice(prompt: str, choices: List[str]) -> str:
    """Ask for a choice from a list of options and re-prompt until valid."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in [choice.lower() for choice in choices]:
            return user_input
        print(f"Please choose from: {', '.join(choices)}")
