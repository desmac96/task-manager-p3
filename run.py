#run.py

import os
import argparse

from src.task_manager import TaskManager
print("Welcome to the task manager")
name=input("What is your name?")
print ("Hello "+name)
response=input ("Choose the following options\n 1. Add a new task \n 2. List all tasks")
if response=="1":

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')
    add_parser.add_argument('--due', type=str, help='Due date of the task in YYYY-MM-DD format')

    # List tasks
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Remove task
    remove_parser = subparsers.add_parser('remove', help='Remove a task by index')
    remove_parser.add_argument('index', type=int, help='Index of the task to remove')

    # Complete task
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete by index')
    complete_parser.add_argument('index', type=int, help='Index of the task to mark as complete')

    args = parser.parse_args()

    task_manager = TaskManager()

    try:
        if args.command == 'add':
            task_manager.add_task(args.description, args.due)
        elif args.command == 'list':
            tasks = task_manager.list_tasks()
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")
        elif args.command == 'remove':
            task_manager.remove_task(args.index)
        elif args.command == 'complete':
            task_manager.mark_task_complete(args.index)
        else:
            parser.print_help()
    except IndexError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

