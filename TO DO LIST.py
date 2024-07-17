class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def remove_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {task}")
        except IndexError:
            print("Invalid task number.")

    def update_task(self, task_number, new_task):
        try:
            old_task = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = new_task
            print(f"Updated task {task_number}: {old_task} -> {new_task}")
        except IndexError:
            print("Invalid task number.")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Update task")
    print("5. Exit")

def main():
    todo_list = TodoList()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '4':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
