# Problem Statement Document

## Problem Statement
College students are constantly juggling assignments, projects, and homework across several courses at once. Standard to-do lists don't work well here because they treat every task like it has the same importance. A 2% quiz due tomorrow is completely different from a 40% final project due next week, but students often struggle to decide where to focus their time first. Without a clear way to rank tasks by actual impact, it's easy to fall into bad time management, last-minute cramming, missed deadlines, and burnout.

## Scope
This project is strictly scoped to a local, Command-Line Interface (CLI) application built for a single user.
* **In-Scope:** Offline data storage using JSON, dynamic priority score calculation, CLI progress reports, and basic CRUD features (add, view, update, delete).
* **Out-of-Scope:** Graphical User Interfaces (GUIs), web/cloud sync, multi-user accounts/auth, SQL databases, or external libraries (like pandas or NumPy).

## Target Users
1. **College and University Students:** Students balancing heavy course loads who need a strategic way to prioritize assignments worth a large chunk of their grade.
2. **High School Students:** Students trying to build better study habits and cut down on overwhelm by focusing on what's due next.
3. **Self-Taught Learners:** Anyone working through bootcamps or online courses who needs a clean system to keep track of their projects and milestones.

## High-Level Features
1. **Core Task Tracking:** Lets users log assignments with key info: Course Code, Title, Deadline, Estimated Completion Time, and Grade Weightage.
2. **Dynamic Priority Algorithm:** A scoring system that calculates urgency using the formula: `Score = (Weightage / (Days Remaining + 1)) * (1 + (Estimated Hours / 10))`. Overdue tasks automatically get tagged as CRITICAL.
3. **Filtered Reporting:** A "Daily Focus" view that picks out and shows only the top 3 most urgent tasks, keeping things clean and simple.
4. **Coursework Health Tracking:** Tracks overall progress across all assignments, rendered as an ASCII progress bar that shows completed weightage vs. total tracked weightage.
5. **Safe File I/O:** Handles reading and writing to `assignments.json` cleanly so data isn't lost or corrupted, even if the file gets accidentally removed or broken.
