from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        task = Task(description, due_date)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        return self.tasks

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
