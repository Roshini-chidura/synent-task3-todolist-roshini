# To-Do List (CLI)

This is a simple to-do list that runs in the terminal, written in Python.
You add tasks, see them listed, tick them off when you finish, and delete the ones you don't need.
Everything is saved in a file, so your tasks are still there when you open the program again.

I made this for Task 3 of my Python Development internship at Synent Technologies.

## What it can do

- Add a task
- Show all your tasks, with [ ] for pending and [x] for done
- Mark a task as done
- Delete a task
- Save your list automatically after every change
- Handle mistakes without crashing, like an empty task, typing letters instead of a number, or choosing a task number that isn't there


## How to run it

1. Install Python 3 (no other libraries are needed).
2. Open a terminal in this project folder.
3. Type `python todo.py` and press Enter.

Your tasks are saved in a file called `tasks.json`, which is created the first time you add a task.


## Sample output

```
---MY TO-DO-LIST---
1. Add a task
2. View task
3. Mark a task as done
4. Delete a task
5. Exit
choose an option (1-5): 2

Your tasks:
1. [x] Finished Python assignment
2. [ ] Record demo video
```