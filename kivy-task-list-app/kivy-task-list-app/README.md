# Kivy Task List Application

This is a simple task list application built using Kivy. The application allows users to add, view, and manage their tasks dynamically.

## Project Structure

```
kivy-task-list-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── ui.kv           # Kivy language layout for the user interface
│   ├── task_manager.py  # Manages the task list
│   └── utils.py        # Utility functions for input validation
├── requirements.txt     # Project dependencies
└── README.md            # Documentation for the project
```

## Features

- Add tasks to the list
- View current tasks
- Clear all tasks

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd kivy-task-list-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- Enter a task in the input field and click the "Add Task" button to add it to the list.
- Click the "Clear Tasks" button to remove all tasks from the list.

## Acknowledgments

This project is built using the Kivy framework. For more information, visit the [Kivy documentation](https://kivy.org/doc/stable/).