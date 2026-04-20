tasks =[
    {"id":1,"task": "clean folder","completed":False},
    {"id":2,"task":"Generate report","completed":False},
    {"id":3,"task":"Scrape website","completed":False}
]
print(tasks)

for task in tasks:
    if task["id"] == 3:
      task["completed"]=True
    print(tasks)
    
import json
with open("tasks.json","w") as f:
    json.dump(tasks,f,indent=4)

    with open("tasks.json","r") as f:
        loaded_tasks = json.load(f)
        print(loaded_tasks)      