#to do list in cmd using python 

tasks = []

def addtask(task):
    tasks.add(task)
    print("Task {task} has been added! ")


def removetask(task):
    if task in tasks:
        tasks.remove(task)
        print("Task {task} has been removed")




def listtask():
    for task in tasks:
        print(task)


while True:
    print("\nOPTIONS:")
    print("1.AddTask")
    print("2.RemoveTask")
    print("3.ListTask")
    print("4.Exit")

    


