# src/task.py

"""
This module defines the Task class for managing individual tasks.
"""

class Task:
    """
    A class to represent a task.

    Attributes:
        description (str): The description of the task.
        completed (bool): The completion status of the task.
        due_date (str, optional): The due date of the task in YYYY-MM-DD format.
    """
    
    def __init__(self, description, due_date=None):
        """
        Initialize a new task with a description and optional due date.

        Args:
            description (str): The description of the task.
            due_date (str, optional): The due date of the task in YYYY-MM-DD format. Defaults to None.
        """
        self.description = description
        self.completed = False
        self.due_date = due_date

    def mark_complete(self):
        """
        Mark the task as complete.
        """
        self.completed = True

    def __str__(self):
        """
        Return a string representation of the task.

        Returns:
            str: The description of the task with its completion status and due date if provided.
        """
        status = "Done" if self.completed else "Not Done"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        return f"{self.description} [{status}{due_date_str}]"
