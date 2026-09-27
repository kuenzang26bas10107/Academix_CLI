"""
task_manager.py
This module contains the Core CRUD (Create, Read, Update, Delete) logic.
It modifies the tasks dictionary in memory.
"""

def generate_id(tasks):
    """
    Generates a new unique ID for a task by finding the highest current ID and adding 1.
    """
    if not tasks:
        return "1"
    
    max_id = max([int(k) for k in tasks.keys()])
    return str(max_id + 1)

def add_task(tasks, course_code, title, deadline_date, estimated_hours, weightage_percent):
    """
    Creates a new task dictionary and adds it to the tasks database.
    """
    new_id = generate_id(tasks)
    
    tasks[new_id] = {
        "id": new_id,
        "course_code": course_code,
        "title": title,
        "deadline_date": deadline_date,
        "estimated_hours": estimated_hours,
        "weightage_percent": weightage_percent,
        "status": "PENDING"
    }
    return new_id

def delete_task(tasks, task_id):
    """
    Removes a task from the database using its ID.
    """
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

def mark_completed(tasks, task_id):
    """
    Updates the status of a specific task to 'COMPLETED'.
    """
    if task_id in tasks:
        tasks[task_id]["status"] = "COMPLETED"
        return True
    return False

def get_all_tasks(tasks):
    """
    Returns all task dictionaries as a list for easy iteration.
    """
    return list(tasks.values())