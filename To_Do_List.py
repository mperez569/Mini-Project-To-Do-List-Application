def display_menu():
    print("""
Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
""")

def add(tasks):
    task = input("Enter the task title: ")
    tasks.append({'title': task, 'status': "Incomplete"})
    print("Task added!")

def view(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['title']} - {task['status']}")

def completed(tasks):
    view(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['status'] = "Complete"
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete(tasks):
    view(tasks)
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
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add(tasks)
            elif choice == '2':
                view(tasks)
            elif choice == '3':
                completed(tasks)
            elif choice == '4':
                delete(tasks)
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
