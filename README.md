# Academix CLI - Academic Deadline & Priority Management Engine

## Overview
Academix CLI is a terminal-based Python application that helps students decide which assignment to work on first. Unlike a standard to-do list, it has an "Urgency Engine" that calculates a priority score for each assignment from its grade weightage, estimated effort and the days left before the deadline. It is built only with Python's standard library, so there is nothing to install apart from Python, and it stores its data in a local JSON file, so it works offline.

## Features
- **Assignment management (CRUD):** add, view, mark as completed, and delete assignments.
- **Urgency Engine:** scores each pending assignment and tags it LOW, MEDIUM, HIGH or CRITICAL (overdue tasks are always CRITICAL).
- **Daily Focus:** shows the top 3 most urgent pending assignments in an ASCII table.
- **Coursework Health Check:** shows the completed share of total tracked weightage with a progress bar.
- **Input validation:** dates, numbers and text are checked, and the prompt repeats until the input is valid.
- **Offline persistence:** data is saved to `assignments.json` after every change and loaded on the next start.

The urgency score is: `Score = (Weightage / (Days Remaining + 1)) * (1 + (Estimated Hours / 10))`. A score of 15 or more is HIGH, 5 or more is MEDIUM, and anything lower is LOW.

## Technologies / Tools Used
- **Python 3:** core language.
- `json`: saving and loading `assignments.json`.
- `datetime`: days remaining and date validation.
- `os`: checking that the data file exists before loading.
- `sys`: clean exit.
- `unittest`: automated tests.
- **Git:** version control.

## Project Structure
```
Academix_CLI/
├── main.py             # entry point, menu loop, input prompts
├── task_manager.py     # add / delete / complete tasks
├── validator.py        # input validation helpers
├── priority_engine.py  # urgency score and priority tag
├── report_service.py   # ASCII tables and progress bar
├── storage.py          # load / save assignments.json
├── test_academix.py    # unit tests
├── statement.md        # problem statement
└── README.md
```

## Steps to Install & Run
1. Install Python 3 (3.8 or newer). Check with `python --version` (or `python3 --version`).
2. Clone the repository and open the folder:
   ```bash
   git clone <your-repository-url>
   cd Academix_CLI
   ```
3. Start the program (no packages to install):
   ```bash
   python main.py
   ```
   On some systems the command is `python3 main.py`.
4. Choose an option from the menu (1-7). `assignments.json` is created automatically the first time you add an assignment.

## Instructions for Testing
### Automated tests
Run the test suite from the project folder:
```bash
python test_academix.py -v
```
All 8 tests should pass. They cover the validators, the priority engine and ID generation.

### Manual testing
- Add an assignment with invalid input (an empty title, a date like `2024-02-30`, a percentage of `150`, hours of `abc`) and check that the prompt repeats.
- Add assignments with different deadlines, mark one as completed, then check options 2, 3 and 4.
- Try completing or deleting an ID that does not exist and check the error message.
- Close and restart the program to confirm the data is still there.

## Non-Functional Requirements
1. **Usability:** a clear text menu, plain prompts, and output formatted as aligned ASCII tables.
2. **Reliability:** only standard-library modules are used, and data is saved after every change.
3. **Maintainability:** the code is split into modules with one job each, and every function has a docstring.
4. **Error handling:** invalid dates, non-numeric input, a missing or corrupted data file, and Ctrl+C are all handled without crashing.

