# Task Tracker

Student: Noor Fatima
Class: AI Engineering, Week 1, Day 2
GitHub repository: https://github.com/noorfatima7082/mini-task-tracker

## Goal

This is a small menu based task tracker in Python. I can add a task, see my tasks, mark one as done, and delete one. My tasks are saved in a file, so they are still there when I run the program again.

## Features

- Add a task. It starts as Pending.
- View all tasks in a numbered list, with Pending or Done next to each one.
- Complete a task by its number.
- Delete a task by its number.
- Save tasks to `tasks.json` and load them again at the start.
- The menu keeps showing until I choose Exit.
- It handles a blank title, a wrong menu choice, a wrong task number, and a missing `tasks.json` file. It shows a short message and keeps going.

## Files

- `mini_task_tracker.py` - the full program
- `tasks.json` - the saved tasks
- `README.md` - this file

## How to run it

You only need Python 3. No extra packages are needed.

### On a laptop

1. Put `mini_task_tracker.py` in a folder.
2. Open a terminal in that folder.
3. Run this:

```
python3 mini_task_tracker.py
```

4. Pick a number from the menu and follow the prompts. Pick 5 to exit.

### In Google Colab

1. Upload `mini_task_tracker.py` to Colab.
2. Run this in a cell:

```
!python3 mini_task_tracker.py
```

3. Pick a number from the menu and follow the prompts. Pick 5 to exit.

One note for Colab: files in Colab are temporary. If you close the runtime, `tasks.json` goes away. To keep it, download `tasks.json` before you close Colab, or save it to Google Drive.

## A short example

```
--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2
1. Read notes [Pending]
Choice: 3
Task number: 1
Task completed.
Choice: 2
1. Read notes [Done]
```

## How the code is built

The tasks are kept in a list. Each task is a small dictionary with a title and a done value, like `{"title": "Read notes", "done": False}`.

The main functions are `load_tasks()`, `save_tasks()`, `add_task()`, `view_tasks()`, `complete_task()` and `delete_task()`. The menu runs in a `while True` loop and uses `if` and `elif` to pick the right function.
