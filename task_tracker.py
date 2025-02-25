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
