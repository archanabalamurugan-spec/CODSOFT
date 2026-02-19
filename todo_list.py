# TO-DO LIST APPLICATION

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nYour To-Do List is empty.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

while True:
    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!\n")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        try:
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!\n")
            else:
                print("Invalid task number.\n")
        except:
            print("Please enter a valid number.\n")

    elif choice == "4":
        show_tasks()
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except:
            print("Please enter a valid number.\n")

    elif choice == "5":
        print("Exiting To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.\n")
