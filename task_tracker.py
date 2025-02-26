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

def add_task():
    #Loading the existing tasks and store in a variable
    tasks = load_tasks()  #tasks is now a list of existing task dictionaries

    if not tasks:  #if the list is empty( python uses if not list to check (boolean)
        new_id = 1
    else:
        #Extract the IDs from the tasks and set new_id to max(existing IDs) + 1
        new_id = max(task['id'] for task in tasks) + 1


    description = input("Enter task description: ")
    #Set a default status
    status = "todo"
    #Generate timestamps for creation and last update
    created_at = datetime.now().isoformat()
    updated_at = created_at  #Initially the updatedAt is the same as createdAt

    #Creating the new task object ( a dictionary) with all necessary fields which then is added to list
    new_task = {
        "id": new_id,
        "description": description,
        "status": status,
        "createdAt": created_at,
        "updatedAt": updated_at
    }

    #Appending the new task to the list of tasks
    tasks.append(new_task)

    #Saving the updated tasks list to the JSON file
    save_tasks(tasks)

    #Provide feedback
    print(f"Task added successfully with ID: {new_id}")

