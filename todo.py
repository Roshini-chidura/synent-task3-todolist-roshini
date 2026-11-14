import json
import os

FILENAME = "tasks.json"

def load_tasks():

    if not os.path.exists(FILENAME):
        return []
    
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read saved tasks. starting with an empty list.")
        return []

def save_tasks(tasks):

    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=2)        

def show_menu():
    print("\n ---MY TO-DO-LIST---")
    print("1. Add a task")
    print("2. View task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def add_task(tasks):
    title = input("what do u need to do? ").strip()
    if title == "":
        print("A task can't be blank.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
        return
    print("\n Your tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{number}. {status} {task['title']}")

def mark_done(tasks):
    if len(tasks) == 0:
        print("There are no tasks to mark")
        return
    view_tasks(tasks)
    choice = input("enter the number of the task you finished: ").strip()
    if not choice.isdigit():
        print("please type a number.")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("there is no task with that number.")
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("nice work! task marked as done.")

def delete_task(tasks):
    if len(tasks) == 0:
        print("there are no tasks to delete")
        return
    view_tasks(tasks)
    choice = input("enter the number of task to delete: ").strip()
    if not choice.isdigit():
        print("please type a number")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("there is no task with that number.")
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice== "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice =="5":
            print("Goodbye!")
            break
        else :
            print("please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()