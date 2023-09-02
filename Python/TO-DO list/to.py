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
choice = input("Enter your choice (1/2/3/4): ")
if choice == "1":
    task = input("Enter the task: ")
    add_task(task)
elif choice == "2":
    task = input("Enter the task to remove: ")
    remove_task(task)
elif choice == "3":
    list_tasks()
elif choice == "4":
    print("Goodbye!")
    exit
else:
    print("Invalid choice. Please select a valid option (1/2/3/4).")    


