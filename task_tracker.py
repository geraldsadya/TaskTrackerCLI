import argparse #this is to handle command line arguments
import json #this is to read/write JSON files
import os #this is to check file existence
from datetime import datetime   #for timestamps

"""logically the first thing we want to do is check if a json file exists and
    if it does we load it and if not we start with an empty list.
"""

#define a variable you want to store the tasks
TASKS_FILE = 'tasks.json'

#function to load tasks

def load_tasks():
    if not os.path.exists(TASKS_FILE): #os method used here don't worry if you don't know it for now
        return [] #if the file does not exist we will return an empty array
    #since it does we read it
    with open(TASKS_FILE, 'r') as f: #opens it but in 'r' which is read mode
        try:
            return json.load(f) #Trying to load and return the JSON data from the file.
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w+') as j: #used w since it allows to write
        json.dump(tasks, j, indent=4) #uses json.dump() to write the tasks list to the file with 4-space indentation

def add_task(description=None):
    tasks = load_tasks()
    if not tasks:
        new_id = 1
    else:
        new_id = max(task['id'] for task in tasks) + 1
    # If a description was provided via command-line, use it; otherwise prompt interactively.
    if description is None:
        description = input("Enter task description: ")
    status = "todo"
    created_at = datetime.now().isoformat()
    updated_at = created_at
    new_task = {
        "id": new_id,
        "description": description,
        "status": status,
        "createdAt": created_at,
        "updatedAt": updated_at
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully with ID: {new_id}")


def update_task(task_id=None, new_description=None):
    tasks = load_tasks()
    if task_id is None:
        task_id = int(input("Enter the ID of the task to update: "))
    if new_description is None:
        new_description = input("Enter the new description: ")
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully!")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id=None):
    tasks = load_tasks()
    if task_id is None:
        task_id = int(input("Enter the ID of the task to delete: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully!")
            return
    print(f"Task with ID {task_id} not found.")


def mark_in_progress(task_id=None):
    tasks = load_tasks()
    if task_id is None:
        task_id = int(input("Enter the ID of the task to mark as in-progress: "))

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "in-progress"
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in-progress!")
            return
    print(f"Task with ID {task_id} not found.")


def mark_done(task_id=None):
    tasks = load_tasks()
    if task_id is None:
        task_id = int(input("Enter the ID of the task to mark as done: "))

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "done"
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done!")
            return
    print(f"Task with ID {task_id} not found.")


def list_tasks(status_filter=None):
    tasks = load_tasks()
    # If a status_filter is provided, filter the tasks accordingly.
    if status_filter:
        tasks = [task for task in tasks if task['status'] == status_filter]

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created At: {task['createdAt']}")
            print(f"Updated At: {task['updatedAt']}")
            print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", nargs="?", help="Description of the new task")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("description", nargs="?", help="New description for the task")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    # Mark in-progress command
    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    mark_in_progress_parser.add_argument("id", type=int, nargs="?", help="ID of the task to mark as in-progress")

    # Mark done command
    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("id", type=int, nargs="?", help="ID of the task to mark as done")

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"], help="Filter tasks by status")

    args = parser.parse_args()

    if args.command == "add":
        add_task(description=args.description)
    elif args.command == "update":
        update_task(task_id=args.id, new_description=args.description)
    elif args.command == "delete":
        delete_task(task_id=args.id)
    elif args.command == "mark-in-progress":
        mark_in_progress(task_id=args.id)
    elif args.command == "mark-done":
        mark_done(task_id=args.id)
    elif args.command == "list":
        list_tasks(status_filter=args.status)

if __name__ == "__main__":
    main()

