tasks = []

def addTask():
    task = input("Enter the task: ")
    tasks.append(task)
    print('Task',task,'added to the list.')
    
    
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks: ")
        for index,task in enumerate(tasks):
            print(f"Task #{index}.{task}")
    
    
def deleteTask():
    listTasks()
    try:
        tasktodelete = int(input("Enter the # to delete: "))
        if tasktodelete >=0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print("Task ",tasktodelete," has been removed.")
        else:
            print("Task",tasktodelete,"was not found.")
    except:
        print("Invalid input.")
    
    
if __name__=="__main__":
    print("Welcome to the To Do list application:")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTasks()
        elif(choice=="4"):
            break
        else:
            print("Invalid input. Please try again")
            
    print("Goodbye 👋👋")