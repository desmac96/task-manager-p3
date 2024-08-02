import argparse
from task_manager import TaskManager


def validate_name(name):
    return name.isalpha()


def get_valid_name():
    while True:
        name = input("What is your name? ")
        if validate_name(name):
            return name
        else:
            print("Invalid name. Please enter alphabetic characters only.")


def interactive_mode():
    task_manager = TaskManager()

    while True:
        print("\nChoose an option:")
        print("1. Add a new task")
        print("2. Task List")
        print("3. Remove a task")
        print("4. Mark Task Completed")
        print("5. Exit")

        response = input("Enter your choice: ")

        if response == "1":
            description = input("Enter the task description: ")
            due_date = input("Enter the due date (DD-MM-YY) or leave blank: ")
            task_manager.add_task(description, due_date if due_date else None)
            print("Task added.")

        elif response == "2":
            tasks = task_manager.list_tasks()
            print("\nTask List:")
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")

        elif response == "3":
            try:
                index = int(input("Enter the index of the task to remove: "))
                task_manager.remove_task(index)
                print("Task removed.")
            except ValueError:
                print("Please enter a valid integer for the index.")
            except IndexError as e:
                print(f"Error: {e}")

        elif response == "4":
            try:
                index = int(input("Enter the index of the task to complete: "))
                task_manager.mark_task_complete(index)
                print("Task marked as complete.")
            except ValueError:
                print("Please enter a valid integer for the index.")
            except IndexError as e:
                print(f"Error: {e}")

        elif response == "5":
            print("Exiting the task manager. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


def main():
    print("Welcome to the task manager")
    name = get_valid_name()
    print("Hello " + name)
    interactive_mode()


if __name__ == "__main__":
    main()
