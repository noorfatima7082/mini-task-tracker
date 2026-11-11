import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("tasks.json was not readable, so I started with an empty list.")
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks):
    title = input("Task title: ").strip()
    if title == "":
        print("Please enter a task title.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        if task["done"]:
            status = "Done"
        else:
            status = "Pending"
        print(str(number) + ". " + task["title"] + " [" + status + "]")


def complete_task(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    view_tasks(tasks)
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Please enter a valid task number.")
        return
    if number < 1 or number > len(tasks):
        print("Please enter a valid task number.")
        return
    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    view_tasks(tasks)
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Please enter a valid task number.")
        return
    if number < 1 or number > len(tasks):
        print("Please enter a valid task number.")
        return
    removed = tasks.pop(number - 1)
    save_tasks(tasks)
    print("Removed: " + removed["title"])


def main():
    tasks = load_tasks()
    while True:
        print()
        print("--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Please choose 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()
