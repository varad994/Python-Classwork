
tasks = []

def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        if tasks:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet!")
    elif choice == '3':
        if tasks:
            task_no = int(input("Enter the task number to delete: "))
            if 0 < task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
