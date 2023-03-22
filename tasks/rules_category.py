import uuid


class RulesCategory:
    def __init__(self, category, rules) -> None:
        self.id = uuid.uuid4()
        self.category = category
        self.rules = []

    def addRule(self, rule):
        self.rules.append(rule)

    def removeRule(self, id):
        indexOfRule = self.rules.index(id)
        self.rules.pop(indexOfRule)
