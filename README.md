# 📝 Task Tracker CLI

![Demo](demo.gif)  
*A simple Python CLI tool to manage tasks using a JSON file.*

## 🚀 Overview
Task Tracker CLI is a command-line application that allows users to **add, update, delete, and manage tasks** efficiently. It supports filtering tasks based on their status and provides a structured way to track pending, in-progress, and completed tasks.

## ⚡ Features
- 📌 **Add Tasks** with unique IDs and descriptions.
- ✏️ **Update Tasks** to modify descriptions.
- 🗑️ **Delete Tasks** by ID.
- ✅ **Mark Tasks** as "in-progress" or "done."
- 📜 **List Tasks** by status (`todo`, `in-progress`, `done`).
- 💾 **Persistent Storage** using a JSON file.
- 🛠️ **Command-Line Interface (CLI)** powered by `argparse`.

## 🛠 Tech Stack
- **Python** (Core Language)
- **argparse** (Command-line argument handling)
- **JSON** (Persistent task storage)

## 📥 Installation
```sh
# Clone the repository
git clone https://github.com/geraldsadya/TaskTrackerCLI.git
cd TaskTrackerCLI

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# Install dependencies (if required)
pip install -r requirements.txt  # (No external libraries, but useful for future expansion)
```

## 🎯 Usage
Run the script with different commands:

### ➕ **Add a Task**
```sh
python task_tracker.py add "Buy groceries"
```
✅ Output: `Task added successfully with ID: 1`

### ✏️ **Update a Task**
```sh
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

### 🚧 **Mark a Task as In Progress**
```sh
python task_tracker.py mark-in-progress 1
```

### ✅ **Mark a Task as Done**
```sh
python task_tracker.py mark-done 1
```

### 🗑️ **Delete a Task**
```sh
python task_tracker.py delete 1
```

### 📜 **List All Tasks**
```sh
python task_tracker.py list
```

### 📂 **List Tasks by Status**
```sh
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## 🎯 Future Improvements
- 🔄 Undo/Redo Feature for task actions.
- 📅 Add Due Dates to tasks.
- 🖥️ Interactive TUI using `curses`.
- 🌐 Web or Mobile Interface Integration.

## 🧑‍💻 Author
**Gerald Sadya**  
📧 sadyageralm@gmail.com 
🔗 https://www.linkedin.com/in/gerald-s-4a9886298/  

## 🤝 Contributing
Feel free to fork the repository and submit pull requests with improvements!

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

