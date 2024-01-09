class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task.title} - {task.description}")

    def delete_task(self, index):
        self.tasks.pop(index - 1)

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Add task\n2. List tasks\n3. Delete task\n4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            index = int(input("Enter task number to delete: "))
            task_manager.delete_task(index)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()