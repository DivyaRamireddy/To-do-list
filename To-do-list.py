# 📝 To-Do List (Console Version)

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "done": False})
    print(f"✅ Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("📭 No tasks yet!")
        return
    print("\n📋 Your Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✔️ Completed" if task["done"] else "⏳ Pending"
        print(f"{idx}. {task['task']} [{status}]")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["done"] = True
        print("🎉 Task marked as completed!")
    except (ValueError, IndexError):
        print("❌ Invalid task number!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"🗑️ Task '{removed['task']}' deleted!")
    except (ValueError, IndexError):
        print("❌ Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
