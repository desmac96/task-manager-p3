# src/task_manager.py

from src.task import Task

class TaskManager:
    def__init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        return self.tasks

    def list_tasks(self):
        return self.list_tasks

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()