tasks = [
    {"id": 1, "task": "clean folder", "Completed":False},
    {"id": 2, "task": "Generate report","Completed": False}
]

while True:
    print("\nTask Manager")
    print("1. Show task")
    print("2.Add task")
    print("3.Complete task")
    print("4.Delete task")
    print("5.Exit")

    choice = input("choose option: ")

    if choice == "1":
        for task in tasks:
            print(tasks)

    elif choice == "2":
        name = input("Enter new task: ")
        new_task = {"id":len(tasks) + 1, "task": name,"completed": False}
        tasks.append(new_task)

    elif choice == "3":
        task_id = int(input("Enter task id to complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True


    elif choice == "4":
        task_id = int(input("Enter task id to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)

    elif choice == "5":
        print("Goodbye.")
        break
