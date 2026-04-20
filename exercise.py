tasks = []
for i in range(3):
    task = input("Enter task: ")
    tasks.append({"task":task,"completed":False})

    print("\n Your tasks:")

    for task in tasks:
        print(task["task"])