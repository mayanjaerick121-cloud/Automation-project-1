tasks = [
    {"id": 1,"task":"clean folder","completed":False},
    {"id": 2,"task":"scrape website",'completed':False},
    {"id": 3,"task":"monitor data","completed":False},
    {"id": 4,"task":"maintain program","completed":False}]

while True:
    print("\n-----TASK MANAGER-----")
    print("1.View task")
    print("2.Add task")
    print("3.Complete task")
    print("4.Delete task")
    print("5.Exit")

    choice = input("Enter option: ")

    if choice == "1":
        for task in tasks:
            print(tasks)
        
    elif choice == "2":
        name = input("Enter new task: ")
        new_task = {"id":len(tasks) +1,"task":name,"completed":False}
        tasks.append(new_task)
        print("Task added successfuly")

    elif choice == "3":
        task_id = int(input("Enter task id to complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task complete successfuly")

    elif choice == "4":
        task_id = int(input("Enter task id to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Deleted successfuly")

    elif choice == "5":
        print("Goodbye user thank for using our task manager!!")
        break
    else:
        print("Invalid option!!")