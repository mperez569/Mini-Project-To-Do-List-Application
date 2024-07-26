#To Do List Application
def display_menu():
    """Display the main menu of the To-Do List Application."""
    print("""
Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
""")

def add_task(tasks):
    """Add a new task to the list with the title 'Incomplete'.

    Args:
        tasks (list): The list of tasks.
    """
    task = input("Enter the task title: ")
    tasks.append({'title': task, 'status': "Incomplete"})
    print("Task added!")

def view_tasks(tasks):
    """View all tasks in the list with their titles and statuses.

    Args:
        tasks (list): The list of tasks.
    """
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['title']} - {task['status']}")

def mark_task_as_complete(tasks):
    """Mark a specific task as complete.

    Args:
        tasks (list): The list of tasks.
    """
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['status'] = "Complete"
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete_task(tasks):
    """Delete a specific task from the list.

    Args:
        tasks (list): The list of tasks.
    """
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    """Main function to handle the To-Do List Application logic."""
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                mark_task_as_complete(tasks)
            elif choice == '4':
                delete_task(tasks)
            elif choice == '5':
                print("Thank you for using the To-Do List App! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Returning to the main menu...")

if __name__ == "__main__":
    main()
