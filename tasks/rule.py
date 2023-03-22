import uuid


class Rule:
    def __init__(self, description) -> None:
        self.id = uuid.uuid4()
        self.description = description
