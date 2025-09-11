class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task and task not in self.tasks:
            self.tasks.append(task)

    def clear_tasks(self):
        self.tasks.clear()

    def get_tasks(self):
        return self.tasks.copy()