# Academix CLI - Academic Deadline & Priority Management Engine

## Overview
Academix CLI is a fully self-contained, terminal-based Python application designed to help students manage their coursework. Unlike a standard to-do list, this application features an underlying "Urgency Engine" that mathematically calculates which assignments need your immediate attention based on deadlines, academic weightage, and estimated effort. It is built strictly using Python's standard library, ensuring a lightweight and robust experience.

## Features
- **Assignment Management (CRUD):** Easily add, view, complete, and delete academic tasks.
- **Urgency Engine Algorithm:** Automatically calculates task priority scores and tags them (e.g., HIGH, CRITICAL) so you know exactly what to work on next.
- **Daily Focus Agenda:** Generates a clean ASCII table of your Top 3 most urgent active assignments to combat task overwhelm.
- **Coursework Health Check:** Displays a progress bar and percentage breakdown of your total completed syllabus weightage.
- **Offline Data Persistence:** Seamlessly saves and loads your agenda locally using a JSON database, ensuring no data is lost between sessions.

## Technologies / Tools Used
- **Python 3:** Core programming language.
- **Built-in `json` library:** For lightweight, offline data persistence (`assignments.json`).
- **Built-in `datetime` library:** For calculating days remaining and validating user input.
- **Built-in `os` library:** For safe file system checks before loading data.
- **Built-in `unittest` library:** For automated validation and logic testing.

## Non-Functional Requirements
1. **Usability:** The application provides a clear, text-based interactive menu. Outputs are formatted into structured, easy-to-read ASCII tables, and prompts for user input are written in plain, beginner-friendly English.
2. **Reliability:** By relying entirely on Python's built-in standard libraries, the application avoids compatibility issues or broken dependencies associated with external packages. It runs reliably on any standard Python 3 installation.
3. **Maintainability:** The codebase is split into distinct, functionally coherent Python modules (e.g., separating file storage logic from mathematical priority logic). This modular design, combined with extensive docstrings, makes the code easy to update or extend.
4. **Error Handling:** The system includes rigorous input validation and `try-except` blocks. It elegantly catches invalid date formats, non-numeric inputs, missing local files, corrupted JSON data, and abrupt user interruptions (like `Ctrl+C`) without crashing the program.

## Instructions for Testing
### 1. Automated Testing
To run the automated test suite and verify the core algorithmic logic and validations, execute the following command in the project directory:
```bash
python test_academix.py
