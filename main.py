"""
This is the entry point of the Academix CLI application.
It connects all the modules together and runs the interactive menu loop.
"""
import sys
import storage
import task_manager
import report_service
import validator

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        is_valid, result = validation_func(user_input)
        if is_valid:
            return result
        else:
            print(f"❌ Error: {result}\n")

def display_menu():
    print("\n" + "*"*40)
    print("🎓 ACADEMIX CLI - Main Menu")
    print("*"*40)
    print("1. Add New Assignment")
    print("2. View Full Agenda")
    print("3. View Daily Focus (Top 3 Urgent)")
    print("4. View Coursework Health Check")
    print("5. Mark Assignment as Completed")
    print("6. Delete an Assignment")
    print("7. Exit Application")
    print("*"*40)

def main():
    print("Starting Academix Engine...")
    tasks = storage.load_data()
    
    while True:
        try:
            display_menu()
            choice = input("Select an option (1-7): ").strip()
            
            if choice == '1':
                print("\n--- Add New Assignment ---")
                course = get_valid_input("Enter Course Code (e.g., CS101): ", validator.is_non_empty_string)
                title = get_valid_input("Enter Assignment Title: ", validator.is_non_empty_string)
                deadline = get_valid_input("Enter Deadline (YYYY-MM-DD): ", validator.is_valid_date)
                hours = get_valid_input("Enter Estimated Hours to Complete: ", validator.is_valid_hours)
                weight = get_valid_input("Enter Weightage Percentage (1-100): ", validator.is_valid_percentage)
                
                task_id = task_manager.add_task(tasks, course, title, deadline, hours, weight)
                storage.save_data(tasks)
                print(f"✅ Success! Assignment added with ID: {task_id}")

            elif choice == '2':
                report_service.print_agenda(tasks)

            elif choice == '3':
                report_service.generate_daily_focus(tasks)
                
            elif choice == '4':
                report_service.generate_health_check(tasks)

            elif choice == '5':
                print("\n--- Mark Completed ---")
                task_id = get_valid_input("Enter ID of assignment to mark completed: ", validator.is_non_empty_string)
                if task_manager.mark_completed(tasks, task_id):
                    storage.save_data(tasks)
                    print(f"✅ Success! Task {task_id} marked as completed.")
                else:
                    print("❌ Error: Task ID not found.")

            elif choice == '6':
                print("\n--- Delete Assignment ---")
                task_id = get_valid_input("Enter ID of assignment to delete: ", validator.is_non_empty_string)
                if task_manager.delete_task(tasks, task_id):
                    storage.save_data(tasks)
                    print(f"✅ Success! Task {task_id} deleted successfully.")
                else:
                    print("❌ Error: Task ID not found.")

            elif choice == '7':
                print("\nExiting Academix Engine. Good luck with your studies! 🚀")
                sys.exit(0)
            else:
                print("❌ Invalid selection. Please enter a number between 1 and 7.")
                
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Saving data and exiting...")
            storage.save_data(tasks)
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
