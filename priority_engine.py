"""
This module acts as the "Urgency Engine". It calculates how critical a task is 
based on a mathematical formula involving deadlines, weightage, and estimated effort.
"""
from datetime import datetime

def calculate_task_priority(task):
    """
    Calculates urgency and assigns a score/tag.
    Formula: Score = (Weightage / (Days Remaining + 1)) * (1 + (Estimated Hours / 10))
    """
    today = datetime.now().date()
    deadline = datetime.strptime(task['deadline_date'], "%Y-%m-%d").date()
    days_remaining = (deadline - today).days

    if task["status"] == "COMPLETED":
        return {"score": 0, "tag": "DONE", "days_remaining": days_remaining}

    if days_remaining < 0:
        return {"score": 9999.0, "tag": "CRITICAL", "days_remaining": days_remaining}

    weightage = task["weightage_percent"]
    hours = task["estimated_hours"]
    score = (weightage / (days_remaining + 1)) * (1 + (hours / 10))

    if score >= 15:
        tag = "HIGH"
    elif score >= 5:
        tag = "MEDIUM"
    else:
        tag = "LOW"

    return {"score": round(score, 2), "tag": tag, "days_remaining": days_remaining}
