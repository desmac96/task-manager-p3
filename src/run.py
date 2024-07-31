import sys
import os
import argparse

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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
            due_date = input("Enter the due date (YYYY-MM-DD) or leave blank: ")
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
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")

    subparsers = parser.add_subparsers(dest='command')

    # Add task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')
    add_parser.add_argument(
        '--due', type=str, help='Due date of the task in YYYY-MM-DD format'
    )

    # List tasks
    subparsers.add_parser('list', help='Task List')

    # Remove task
    remove_parser = subparsers.add_parser('remove', help='Remove a task by index')
    remove_parser.add_argument('index', type=int, help='Index of the task to remove')

    # Complete task
    complete_parser = subparsers.add_parser('complete', help='Mark Task Completed')
    complete_parser.add_argument('index', type=int, help='Index of the task to mark as complete')

    args = parser.parse_args()

    task_manager = TaskManager()

    try:
        if args.command == 'add':
            task_manager.add_task(args.description, args.due)
        elif args.command == 'list':
            tasks = task_manager.list_tasks()
            print("\nTask List:")
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")
        elif args.command == 'remove':
            try:
                task_manager.remove_task(args.index)
                print("Task removed.")
            except IndexError as e:
                print(f"Error: {e}")
        elif args.command == 'complete':
            try:
                task_manager.mark_task_complete(args.index)
                print("Task marked as complete.")
            except IndexError as e:
                print(f"Error: {e}")
        else:
            print("Welcome to the task manager")
            name = get_valid_name()
            print("Hello " + name)
            interactive_mode()
    except IndexError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
