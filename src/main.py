# src/main.py 

import argparse 

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    args = parser.parse_args()

import argparse

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    subparsers = parser.add_subparsers(dest='command')

# src/main.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

import argparse

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # List tasks
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # src/main.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # List tasks
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Remove task
    remove_parser = subparsers.add_parser('remove', help='Remove a task by index')
    remove_parser.add_argument('index', type=int, help='Index of the task to remove')

# src/main.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # List tasks
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Remove task
    remove_parser = subparsers.add_parser('remove', help='Remove a task by index')
    remove_parser.add_argument('index', type=int, help='Index of the task to remove')

    # Complete task
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete by index')
    complete_parser.add_argument('index', type=int, help='Index of the task to mark as complete')

# src/main.py

import argparse
from src.task_manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List Application")
    
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

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

    if args.command == 'add':
        task_manager.add_task(args.description)
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

if __name__ == '__main__':
    main()
