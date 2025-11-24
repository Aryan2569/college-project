tasks = []

def add_task():
    """Adds a new task to the list."""
    print("\n--- Add New Task ---")
    name = input("Enter Task Description: ").strip()
    
    if name:
        new_task = {'name': name, 'completed': False}
        tasks.append(new_task)
        print(f"\n✅ Task '{name}' added.")
    else:
        print("\nTask cannot be empty.")

def view_tasks():
    """Displays all tasks."""
    if not tasks:
        print("\n📝 Your task list is currently empty.")
        return

    print("\n" + "="*30)
    print("      COLLEGE TASK LIST")
    print("="*30)

    for i, task in enumerate(tasks):
        status = "[DONE]" if task['completed'] else "[OPEN]"
        print(f"{i+1}. {status:<6} | {task['name']}")
    
    print("="*30)

def mark_complete():
    """Marks a task as completed."""
    if not tasks:
        print("No tasks to mark as complete.")
        return
    
    view_tasks() # Show the tasks so the user can see the numbers

    try:
        task_index = int(input("\nEnter the number of the task to mark as COMPLETE: ")) - 1
        
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            print(f"\n🎉 Task '{tasks[task_index]['name']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    """Deletes a task."""
    if not tasks:
        print("No tasks to delete.")
        return
    
    view_tasks() # Show the tasks so the user can see the numbers

    try:
        task_index = int(input("\nEnter the number of the task to DELETE: ")) - 1
        
        if 0 <= task_index < len(tasks):
            deleted_task_name = tasks[task_index]['name']
            del tasks[task_index]
            print(f"\n🗑️ Task '{deleted_task_name}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# --- Main Application Loop ---

def main():
    """Runs the main menu loop."""
    print("Welcome to the Simple Task Manager!")

    while True:
        print("\n\n=== Task Manager Menu ===")
        print("1. View All Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nGoodbye! The task list is cleared when you exit.")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()