# Academix CLI - Academic Deadline & Priority Management Engine

## Overview
Academix CLI is a terminal-based Python tool I built to help figure out what assignment to start working on first. Instead of acting like a basic to-do list, it calculates a priority score for each assignment based on how much it's worth (grade weight), how long it'll take, and how close the deadline is. Built entirely with Python's standard library, so you don't need to install any external dependencies. It saves everything locally in a JSON file, so it works completely offline.

## Features
- **Assignment management (CRUD):** Add, view, mark as done, and delete assignments.
- **Urgency Engine:** Calculates a score for pending tasks and tags them as LOW, MEDIUM, HIGH, or CRITICAL (anything overdue automatically becomes CRITICAL).
- **Daily Focus:** Pulls up your top 3 most urgent pending tasks formatted in an ASCII table.
- **Coursework Health Check:** Uses a progress bar to show how much total course weightage you've finished so far.
- **Input validation:** Catches bad inputs for dates, numbers, and text, re-prompting until you get it right.
- **Offline persistence:** Automatically saves changes to `assignments.json` after every update and reloads them when you restart.

The urgency formula works like this: `Score = (Weightage / (Days Remaining + 1)) * (1 + (Estimated Hours / 10))`. A score of 15+ triggers HIGH, 5+ triggers MEDIUM, and anything below that is LOW.

## Technologies / Tools Used
- **Python 3:** Main language.
- `json`: Handles saving and loading `assignments.json`.
- `datetime`: Tracks remaining days and validates date formats.
- `os`: Checks if the JSON data file exists before attempting to load.
- `sys`: Handles clean exits.
- `unittest`: Runs automated testing.
- **Git:** Version control.

## Project Structure
```
Academix_CLI/
├── main.py          # Entry point, menu loop, and CLI prompts
├── task_manager.py  # Logic for adding, deleting, and completing tasks
├── validator.py     # Helpers for checking user input
├── priority_engine.py # Calculates urgency score and assigns priority tags
├── report_service.py # Generates ASCII tables and progress bars
├── storage.py       # Reads and writes to assignments.json
├── test_academix.py # Unit test suite
├── statement.md     # Problem statement writeup
└── README.md
```

## Steps to Install & Run
1. Make sure you have Python 3 (3.8 or newer) installed. Verify by running `python --version` (or `python3 --version`).
2. Clone the repo and move into the project directory:
   ```bash
   git clone <your-repository-url>
   cd Academix_CLI
   ```
3. Run the script (no pip install needed):
   ```bash
   python main.py
   ```
   *(Note: Depending on your system setup, you might need to run `python3 main.py` instead).*
4. Pick an option (1–7) from the menu. The program will automatically create `assignments.json` the first time you add an assignment.

## Instructions for Testing
### Automated tests
To run the automated tests from the project root:
```bash
python test_academix.py -v
```
All 8 tests should pass successfully. They verify input validation, priority calculations, and ID generation logic.

### Manual testing
- Try entering invalid inputs when adding a task (like an empty title, impossible dates like `2024-02-30`, weightage over `150`, or letters for hours like `abc`) to ensure the validation prompts loop properly.
- Add tasks with various deadlines, complete one, and check options 2, 3, and 4 to verify the output.
- Try completing or deleting an ID that doesn't exist to make sure the error handling catches it.
- Exit and restart the application to confirm your saved assignments persist.

## Non-Functional Requirements
1. **Usability:** Features a simple text-based menu, straightforward prompts, and clean ASCII table outputs.
2. **Reliability:** Uses zero external dependencies and automatically saves data after every change.
3. **Maintainability:** Modular architecture where each file handles a single responsibility, fully documented with docstrings across all functions.
4. **Error handling:** Built to handle bad dates, wrong data types, missing/corrupted files, and sudden interrupts like `Ctrl+C` without crashing.
