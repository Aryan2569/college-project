tasks = []
def list_tasks(tasks):
    "Displays the current list of tasks, sorting incomplete tasks to the top."   
    if not tasks:
        print("\n Your to-do list is empty... Add a task to get started.")
        return
    sorted_tasks = sorted(tasks, key=lambda x: x['done'])
    print("\n--- Daily To-Do List ---")
    for index, task in enumerate(sorted_tasks):
        status = " DONE" if task['done'] else "☐ PENDING"
        print(f"{index + 1}. [{status}] {task['description']}")
    print("------------------------\n")
def add_task(tasks):
    "Enter your task to add it to list."
    description = input("Enter the task pending: ").strip()
    if description:
        new_task = {
            'description': description,
            'done': False
        }
        tasks.append(new_task)
        print(f" Task '{description}' added.")
    else:
        print("Invalid input...Add a task")
def mark_done(tasks):
    "Allows the user to mark a task as complete using the displayed index."   
    sorted_tasks = sorted(tasks, key=lambda x: x['done'])
    if not sorted_tasks:
        list_tasks(tasks)
        return
    list_tasks(tasks)
    try:
        task_num = int(input("Enter the serial number of task which u completed (or 0 to cancel): "))   
        if task_num == 0:
            return
        task_index = task_num - 1       
        if 0 <= task_index < len(sorted_tasks):
            task = sorted_tasks[task_index]           
            task['done'] = True
            print(f" Task '{task['description']}' marked as completed")
        else:
            print("Invalid task number.")
    except ValueError:
        print(" Invalid input. Please enter a number.")
def main() :
    "The main application loop."
    print("--- Simple Python Task Manager ---")
    while True:
        print("\n--- Menu ---")
        print("1. List tasks")
        print("2. Add new task")
        print("3. Mark the completed task")
        print("4. Exit")       
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            print("\nExiting. Note: Tasks are not saved. Goodbye")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()