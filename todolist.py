class TodoList:
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self._tasks):
            removed_task = self._tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")

    def display_tasks(self):
        print("\nTo-Do List:")
        if not self._tasks:
            print("You have no tasks in your list.")
        else:
            print("Your tasks:")
            for i, task in enumerate(self._tasks, start=1):
                print(f"{i}. {task}")

def main():
    print("How would you like to manage your tasks?")
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your new task: ")
            todo_list.add(task)
        elif choice == "2":
            if not todo_list._tasks:
                print("You have no tasks in your list.")
            else:
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    todo_list.remove_task(task_num)
                except ValueError:
                    print("Invalid task number.")
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()
  
