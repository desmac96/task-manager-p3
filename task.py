from datetime import datetime


class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = datetime.strptime(due_date, "%d-%m-%y")
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return (
            f"{self.description} (Due: {self.due_date}, "
            f"Completed: {'✓' if self.completed else '✗'})"
        )
