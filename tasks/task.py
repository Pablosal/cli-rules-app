import uuid


class Task:
    def __init__(self, description, done, priority):
        self.id = uuid.uuid4()
        self.description = description
        self.done = done
        self.priority = priority

    def __str__(self):
        return self.description


task = Task("hacer la tarea", False, "medium")
