tasks = []

def addtask(task):
    tasks.append(task)
    print("Task {task} has been added!")

def removetask(task):
    if task in tasks:
        tasks.remove(task)
        print("Task {task} has been removed.")
    else:
        print("Task {task} not found.")

def listtask():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print("{index}. {task}")
    else:
        print("No tasks to display.")

while True:
    print("\nOPTIONS:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        task = input("Enter the task: ")
        addtask(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        removetask(task)
    elif choice == "3":
        listtask()
    elif choice == "4":
        print("Goodbye!")
        break  
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
    


