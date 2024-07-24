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