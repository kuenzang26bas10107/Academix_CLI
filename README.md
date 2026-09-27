# Academix CLI - Academic Deadline & Priority Management Engine

## Overview
Academix CLI is a fully self-contained, terminal-based Python application designed to help students manage their coursework. Unlike a standard to-do list, this application features an underlying "Urgency Engine" that mathematically calculates which assignments need your immediate attention based on deadlines, academic weightage, and estimated effort. It is built strictly using Python's standard library, ensuring a lightweight and robust experience.

## Features
*   **Assignment Management (CRUD):** Easily add, view, complete, and delete academic tasks.
*   **Urgency Engine Algorithm:** Automatically calculates task priority scores and tags them (e.g., HIGH, CRITICAL) so you know exactly what to work on next.
*   **Daily Focus Agenda:** Generates a clean ASCII table of your Top 3 most urgent active assignments to combat task overwhelm.
*   **Coursework Health Check:** Displays a progress bar and percentage breakdown of your total completed syllabus weightage.
*   **Offline Data Persistence:** Seamlessly saves and loads your agenda locally using a JSON database, ensuring no data is lost between sessions.

## Non-Functional Requirements
1.  **Usability:** The application provides a clear, text-based interactive menu. Outputs are formatted into structured, easy-to-read ASCII tables, and prompts for user input are written in plain, beginner-friendly English.
2.  **Reliability:** By relying entirely on Python's built-in standard libraries (like `datetime` and `json`), the application avoids compatibility issues or broken dependencies associated with external packages like pandas. It runs reliably on any standard Python 3 installation.
3.  **Maintainability:** The codebase is split into exactly six distinct, functionally coherent Python modules (e.g., separating file storage logic from mathematical priority logic). This modular design, combined with extensive docstrings and inline comments, makes the code easy to update or extend.
4.  **Error Handling:** The system includes rigorous input validation and `try-except` blocks. It elegantly catches invalid date formats, non-numeric inputs, missing local files, corrupted JSON data, and abrupt user interruptions (like `Ctrl+C`) without crashing the program.

## Installation and Setup Steps
1.  Ensure you have Python 3 installed on your computer. (You can check this by typing `python --version` in your terminal).
2.  Download or extract the project folder containing the 6 `.py` files and 2 `.md` files.
3.  Open your operating system's Terminal or Command Prompt.
4.  Use the `cd` command to navigate to the directory where you extracted the project files.

## Execution Command
Once you are inside the project folder in your terminal, run the following exact command to launch the application:

```bash
python main.py
```
*(Note: Depending on your system configuration, you may need to use `python3 main.py`)*