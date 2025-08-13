# Vocabulary Builder

Welcome to your first Python project! This is a simple command-line application that helps you learn basic Python programming concepts.

## What You'll Build

A basic vocabulary app where you can:
- Add new words with their meanings
- View all your words
- Take simple quizzes
- Save your data

## Quick Start

### 1. **Setup**
- Make sure Python is installed on your computer
- Download this project folder
- Open Command Prompt (Windows) or Terminal (Mac/Linux)

### 2. **Test Python**
```cmd
# Windows
python --version

# Mac/Linux  
python3 --version
```

### 3. **Run the App**
```cmd
# Windows
python -m vocab_builder

# Mac/Linux
python3 -m vocab_builder
```

If you don't have pytest and want to run the tests:
```cmd
pip install pytest
```

## Learning Path - Simple Steps

### **Step 1: Basic Input & Output** - COMPLETED
- [x] Menu shows up
- [x] You can type numbers to choose options
- [x] App exits when you choose 0

### **Step 2: Add Words** - IMPLEMENT THIS
**File:** `vocab_builder/features/add_word.py`
**What to do:** Make the word input work better
```python
def collect_word():
    word = ask_str("Enter word: ")
    
    # TODO: Add simple validation here
    # - Check if word is not empty
    # - Check if word is not too long (more than 20 letters)
    # - Give helpful error message if wrong
    
    meaning = ask_str("Enter meaning: ")
    # TODO: Add simple validation here too
```

### **Step 3: View Words** - IMPLEMENT THIS
**File:** `vocab_builder/features/view_words.py`
**What to do:** Show words in a nice way
```python
def run():
    # TODO: Make this look better
    # - Show each word on a new line
    # - Add some spacing between words
    # - Show "No words yet!" if list is empty
```

### **Step 4: Simple Quiz** - IMPLEMENT THIS
**File:** `vocab_builder/features/quiz.py`
**What to do:** Make quiz questions work
```python
def make_mcq_question(words):
    # TODO: Make this simpler
    # - Pick one random word
    # - Show the word and ask "What does this mean?"
    # - Give 2 choices: correct meaning + 1 wrong meaning
```

### **Step 5: Save Data** - IMPLEMENT THIS
**File:** `vocab_builder/utils/store.py`
**What to do:** Handle file errors better
```python
def read_json(path):
    # TODO: Add simple error message
    # - If file is broken, show "File is broken, starting fresh"
    # - Don't crash the app
```

## Testing Your Code

### **Simple Test**
1. Run the app: `python -m vocab_builder`
2. Choose option 1 (Add word)
3. Add a word like "hello" with meaning "a greeting"
4. Choose option 2 (View words) - see if your word shows up
5. Choose option 3 (Quiz) - see if quiz works

### **What to Check**
- [ ] Can you add words without errors?
- [ ] Do words show up when you view them?
- [ ] Does quiz ask questions?
- [ ] Does app save your words between runs?

## Common Problems

### **Python Not Found**
```cmd
# Try these instead:
python3 --version
py --version
```

### **Import Error**
```cmd
# Make sure you're in the right folder
cd Python_Course_Project
python -m vocab_builder
```

### **App Crashes**
- Check if you have at least 1 word added
- Look at error messages in the console
- Try deleting the data files and restart

## Success Checklist

**You're done when:**
- [ ] Menu works without crashing
- [ ] You can add words
- [ ] You can see your words
- [ ] Quiz asks questions
- [ ] App saves your data

## Tips for Beginners

1. **Start small** - Get one feature working before moving to the next
2. **Test often** - Run your code after each small change
3. **Read error messages** - They tell you what's wrong
4. **Ask for help** - Programming is hard, everyone needs help!

## Ready to Start?

**Begin with Step 2** - just make the word input a little better. Don't worry about making it perfect, just make it work!

**Remember:** This is your first project. It's okay if it's not perfect. Focus on learning and having fun!

---

*Need help? Look at the TODO comments in each file - they tell you exactly what to do!*


