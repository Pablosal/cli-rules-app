import json
import uuid


class FileModificationManager:
    def __init__(self, filename):
        self.filename = filename

    def category_exists(self, category):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return any(x["category"] == category for x in data)

    def create_new_category(self, category):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            data.append({"category": category, "rules": []})
        self._write_to_file(data)
        return data

    def add_new_rule(self, rule, category):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            for item in data:
                if item["category"] == category:
                    item["rules"].append(
                        {"id": str(uuid.uuid4()), "name": rule})
                    self._write_to_file(data)
                    return data

    def get_rules_from(self, category):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            for item in data:
                if item["category"] == category:
                    print("Inicio de Reglas")
                    for rule in item["rules"]:
                        print('\033[94m' + "[ ] " + rule["name"])
                    return
            else:
                print("No han sido encontrado el tema")
                return []

    def get_all_values(self):
        with open(self.filename, 'r') as f:
            themesjson = json.load(f)
            print("Here are the themes")
            for theme in themesjson:
                tema = theme["category"]
                print(f"{tema}")
            return

    def _write_to_file(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
