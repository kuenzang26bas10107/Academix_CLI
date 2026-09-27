# Problem Statement Document

## Problem Statement
Students constantly juggle multiple academic assignments, projects, and homework across various courses. Traditional to-do lists fail because they treat all tasks equally. A 2% quiz due tomorrow is vastly different from a 40% final project due next week, yet students often struggle to allocate their time efficiently between them. This lack of quantitative prioritization leads to poor time management, last-minute cramming, missed deadlines, and severe academic burnout. 

## Scope
The scope of this project is strictly limited to a local, Command-Line Interface (CLI) application. It is designed as a single-user productivity tool. 
*   **In-Scope:** Offline data storage via JSON, mathematical priority calculation, CLI-based progress reporting, and basic CRUD operations.
*   **Out-of-Scope:** Graphical User Interfaces (GUIs), web/cloud synchronization, multi-user authentication, SQL databases, and the use of third-party external libraries (e.g., pandas, NumPy).

## Target Users
1.  **University and College Students:** Individuals balancing heavy credit loads who need to strategically distribute their effort across assignments with high grade weightages.
2.  **High School Students:** Students looking to build better time-management habits and reduce anxiety by focusing only on the most immediate tasks.
3.  **Self-Taught Learners:** Individuals progressing through bootcamps or online certifications who need an organized way to track their modular milestones.

## High-Level Features
1.  **Core Task Tracking:** The ability to log assignments with specific attributes: Course Code, Title, Deadline, Estimated Completion Hours, and Total Grade Weightage.
2.  **Dynamic Priority Algorithm:** A mathematical engine that calculates a precise urgency score using the formula: `Score = (Weightage / (Days Remaining + 1)) * (1 + (Estimated Hours / 10))`. Overdue tasks are automatically flagged as CRITICAL.
3.  **Filtered Reporting:** Generation of a "Daily Focus" view that isolates and displays only the top 3 most urgent tasks, eliminating visual clutter and decision fatigue.
4.  **Quantitative Health Tracking:** A calculation of overall coursework completion, visually represented by an ASCII progress bar mapping completed weightage against total tracked weightage.
5.  **Safe File I/O:** Robust reading and writing of `assignments.json` to ensure user data is consistently saved and recovered safely, even if the file is manually deleted or corrupted.