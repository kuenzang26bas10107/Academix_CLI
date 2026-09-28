"""
This module handles all the output formatting.
It renders data into clean ASCII tables and progress bars for the CLI.
"""
import priority_engine

def print_row(cols, widths):
    row = "|"
    for col, width in zip(cols, widths):
        text = str(col)[:width-2].ljust(width-2)
        row += f" {text} |"
    print(row)

def print_separator(widths):
    total_width = sum(widths) + (len(widths) * 3) + 1
    print("-" * total_width)

def print_agenda(tasks):
    print("\n" + "="*80)
    print(" ACADEMIC AGENDA ".center(80, "="))
    print("="*80)

    if not tasks:
        print("No tasks found. Add some to get started!")
        return

    widths = [6, 12, 18, 14, 8, 8, 12]
    headers = ["ID", "Course", "Title", "Deadline", "Hrs", "Weight", "Status"]
    
    print_separator(widths)
    print_row(headers, widths)
    print_separator(widths)

    for t in tasks.values():
        row_data = [
            t['id'], t['course_code'], t['title'], 
            t['deadline_date'], t['estimated_hours'], 
            f"{t['weightage_percent']}%", t['status']
        ]
        print_row(row_data, widths)
    
    print_separator(widths)

def generate_daily_focus(tasks):
    print("\n" + "="*70)
    print(" DAILY FOCUS (Top 3 Urgent Tasks) ".center(70, "="))
    print("="*70)

    active_tasks = [t for t in tasks.values() if t["status"] != "COMPLETED"]
    
    if not active_tasks:
        print("No pending tasks! You are all caught up.")
        return

    enriched_tasks = []
    for task in active_tasks:
        priority_data = priority_engine.calculate_task_priority(task)
        enriched_task = {**task, **priority_data}
        enriched_tasks.append(enriched_task)
        
    enriched_tasks.sort(key=lambda x: x["score"], reverse=True)
    top_3 = enriched_tasks[:3]

    widths = [6, 12, 18, 12, 12]
    headers = ["ID", "Course", "Title", "Days Left", "Priority"]
    
    print_separator(widths)
    print_row(headers, widths)
    print_separator(widths)
    
    for t in top_3:
        print_row([t['id'], t['course_code'], t['title'], t['days_remaining'], t['tag']], widths)
    print_separator(widths)

def generate_health_check(tasks):
    print("\n" + "="*70)
    print(" COURSEWORK HEALTH CHECK ".center(70, "="))
    print("="*70)
    
    if not tasks:
        print("No tasks tracked yet.")
        return
        
    total_weight = sum(t['weightage_percent'] for t in tasks.values())
    completed_weight = sum(t['weightage_percent'] for t in tasks.values() if t['status'] == "COMPLETED")
    
    if total_weight == 0:
        print("Total tracked weightage is 0%. Add weightages to see progress.")
        return
        
    completion_ratio = (completed_weight / total_weight) * 100
    
    print(f"Total Tracked Weightage : {total_weight}%")
    print(f"Completed Weightage     : {completed_weight}%")
    print(f"Overall Progress        : {completion_ratio:.2f}%\n")
    
    bar_length = 40
    filled_length = int((completion_ratio / 100) * bar_length)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    print(f"[{bar}] {completion_ratio:.1f}%")
    print("="*70)
