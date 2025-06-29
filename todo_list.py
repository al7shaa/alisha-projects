todo_list = []

def show_menu():
    print("\nWhat would you like to do?")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        if not todo_list:
            print("No tasks yet.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter task to add: ")
        todo_list.append(task)
        print(f"Added: {task}")

    elif choice == '3':
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
