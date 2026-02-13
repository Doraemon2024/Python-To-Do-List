
# To-Do List 

import os

FILE_NAME = "tasks.txt"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def header(title):
    print("=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)


def view_tasks(tasks):
    clear_screen()
    header("📋 YOUR TO-DO LIST")

    if not tasks:
        print("\n🌱 No tasks yet. Add something!\n")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f" {i}. ✅ {task}")

    input("\n🔁 Press Enter to return to menu...")


def add_task(tasks):
    clear_screen()
    header("➕ ADD NEW TASK")

    task = input("✍️ Enter task description: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("\n🎉 Task added successfully!")
    else:
        print("\n⚠️ Task cannot be empty.")

    input("\n🔁 Press Enter to return to menu...")


def remove_task(tasks):
    clear_screen()
    header("🗑️ REMOVE TASK")

    if not tasks:
        print("\n⚠️ No tasks to remove.")
        input("\n🔁 Press Enter to return to menu...")
        return

    for i, task in enumerate(tasks, start=1):
        print(f" {i}. ❌ {task}")

    try:
        choice = int(input("\n👉 Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"\n🧹 Task '{removed}' removed!")
        else:
            print("\n⚠️ Invalid task number.")
    except ValueError:
        print("\n⚠️ Please enter a valid number.")

    input("\n🔁 Press Enter to return to menu...")


def main():
    tasks = load_tasks()

    while True:
        clear_screen()
        header("📝 TO-DO LIST MANAGER")

        print(" 1️⃣  View Tasks")
        print(" 2️⃣  Add Task")
        print(" 3️⃣  Remove Task")
        print(" 4️⃣  Exit")

        print("\n" + "-" * 40)
        choice = input("👉 Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            clear_screen()
            header("👋 THANK YOU")
            print("\n✨ Your tasks are saved safely.\n")
            break
        else:
            print("\n⚠️ Invalid choice!")
            input("🔁 Press Enter to try again...")


if __name__ == "__main__":
    main()