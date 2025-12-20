# To-Do List Application (Command Line)

tasks = []

def show_menu():
    print("\n*****TO-DO LIST MENU*****")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("***************************")

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    new_task = input("\nEnter the new task: ")
    tasks.append(new_task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    if len(tasks) == 0:
        return
    
    try:
        task_no = int(input("\nEnter the task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_value = input("Enter updated task: ")
            tasks[task_no - 1] = new_value
            print("Task updated!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    
    try:
        task_no = int(input("\nEnter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


while True:
    show_menu()
    try:
        choice = int(input("Choose an option (1-5): "))
        if choice == 1:
            view_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            update_task()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1-5.")
    except ValueError:
        print("Please enter a valid number!")

