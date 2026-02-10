# Command-Line Task Manager
import datetime
import os
import datetime 
#File to store tasks
FILE_NAME="tasks.txt"

#load tasks from file
def load_tasks():
    tasks={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            for line in file:
                task_id,title,status,deadline=line.strip().split(" | ")
                tasks[int(task_id)]={"title":title,"status":status, "deadline":None if deadline=="None" else deadline}
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        for task_id,task in tasks.items():
            deadline=task["deadline"] if task["deadline"] else "None"
            file.write(f"{task_id} | {task['title']} | {task['status']} | {deadline}\n")

# Add a new task
def add_task(tasks):
    title=input("Enter task title:")
    task_id=max(tasks.keys(),default=0) +1
    tasks[task_id]={"title":title,"status":"incomplete","deadline":None}
    print(f"Task '{title}' added.")

#View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        for task_id,task in tasks.items():
            deadline = task["deadline"] if task["deadline"] else "No deadline"
            print(f"[{task_id}] {task['title']} - {task['status']} - {deadline}")

#Mark task as complete
def mark_task_complete(tasks):
    task_id=int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"]="complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found")

#Delete a task
def delete_task(tasks):
    task_id=int(input("Enter task ID to mark as Delete: "))
    if task_id in tasks:
        deleted_task=tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task ID not found")

# Main Menu
def main():
    tasks=load_tasks()
    while True:
        print("\nTask Manager Menu: ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Add Deadline")
        print("6. Exit")

        choice=input("Enter your choice:")

        match choice:
            case "1":
                add_task(tasks)
            case "2":
                view_tasks(tasks)
            case "3":
                mark_task_complete(tasks)
            case "4":
                delete_task(tasks)
            case "5":
                add_deadlines(tasks)
            case "6":
                save_tasks(tasks)
                break
            case _:
                print("Invalid Choice. Please try again")

# Add deadlines done by Purna
def add_deadlines(tasks):
    task_id = int(input("Enter task ID to add deadline: "))

    if task_id not in tasks:
        print("Task ID not found")
        return

    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))

    deadline = datetime.datetime(year, month, day, hour, minute)

    if deadline < datetime.datetime.now():
        print("Deadline cannot be in the past.")
        return

    tasks[task_id]["deadline"] = deadline.isoformat()
    print("Deadline added successfully.")



if __name__ =="__main__":
    main()