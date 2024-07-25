# src/task_manager.py

"""
This module defines the TaskManager class for managing a list of tasks.
"""

from src.task import Task

class TaskManager:
    """
    A class to manage a list of tasks.
    """
    
    def __init__(self):
        """Initialize the TaskManager with an empty list of tasks."""
        self.tasks = []

    def add_task(self, description, due_date=None):
        """
        Add a new task to the task list.

        Args:
            description (str): The description of the task.
            due_date (str, optional): The due date of the task in YYYY-MM-DD format. Defaults to None.

        Raises:
            ValueError: If the task description is empty.
        """
        if not description:
            raise ValueError("Task description cannot be empty")
        task = Task(description, due_date)
        self.tasks.append(task)

    def remove_task(self, index):
        """
        Remove a task from the task list by its index.

        Args:
            index (int): The index of the task to remove.

        Raises:
            IndexError: If the task index is out of range.
        """
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Task index out of range")
        self.tasks.pop(index)

    def list_tasks(self):
        """
        List all tasks.

        Returns:
            list: A list of all tasks.
        """
        return self.tasks

    def mark_task_complete(self, index):
        """
        Mark a task as complete by its index.

        Args:
            index (int): The index of the task to mark as complete.

        Raises:
            IndexError: If the task index is out of range.
        """
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Task index out of range")
        self.tasks[index].mark_complete()
