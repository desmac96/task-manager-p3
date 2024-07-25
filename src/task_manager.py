# src/task_manager.py

from src.task import Task

class TaskManager:
    def__init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        if not description:
            raise ValueError("Task description cannot be empty")
        task = Task(description, due_date)
        self.tasks.append(task)

    def remove_task(self, index):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Task index out of range")
        self.tasks.pop(index)

    def list_tasks(self):
        return self.tasks

    def list_tasks(self):
        return self.list_tasks

    def mark_task_complete(self, index):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Task index out of range") 
        self.tasks[index].mark_complete()