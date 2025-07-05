import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for line in f:
                task, status = line.strip().split("||")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['task']}||{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "[\u2714]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

def add_task(tasks):
    task_name = input("Enter new task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added successfully.")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as complete.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f"Task '{removed['task']}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
