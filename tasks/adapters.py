from .models import Task

class TaskConsoleAdapter:
    def __init__(self,task):
        self.task=task

    def format_for_console(self):
        return f"Task: {self.task.title} - {self.task.description}"    