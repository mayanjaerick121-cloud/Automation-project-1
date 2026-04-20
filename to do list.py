# To-Do List Application

def display_menu():
    """Display the menu"""
    print("\n" + "=" * 50)
    print("📝 TO-DO LIST MANAGER")
    print("=" * 50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 50)


def add_task(tasks):
    """Add a new task"""
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f"✓ Task '{task}' added successfully!")
    else:
        print("❌ Task cannot be empty!")


def view_tasks(tasks):
    """View all tasks"""
    if not tasks:
        print("\n📭 No tasks yet!")
        return
    
    print("\n" + "=" * 50)
    print("YOUR TASKS:")
    print("=" * 50)
    for i, item in enumerate(tasks, 1):
        status = "✓" if item["completed"] else "○"
        print(f"{i}. [{status}] {item['task']}")
    print("=" * 50)


def mark_complete(tasks):
    """Mark a task as complete"""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to mark complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"✓ Task marked as complete!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")


def delete_task(tasks):
    """Delete a task"""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted = tasks.pop(task_num - 1)
                print(f"✓ Task '{deleted['task']}' deleted!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")


def main():
    tasks = []
    
    print("\n🎉 Welcome to To-Do List Manager!")
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Thank you for using To-Do List Manager! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
