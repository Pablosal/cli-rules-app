import click
from filemanager import FileModificationManager
rulesfile = "themerules.json"


@click.command()
def show_themes():
    manager = FileModificationManager(filename=rulesfile)
    manager.get_all_values()


@click.command()
@click.option("--category", prompt="Enter the category you are searching", help="The name of the category")
@click.option("-r", prompt="Enter the rule of the category", help="The description of the rule")
def add_rules(category, r):
    manager = FileModificationManager(filename=rulesfile)
    if manager.category_exists(category):
        manager.add_new_rule(r, category)
    else:
        print("There is no category with that name, do you wish to create it?")
        desition = input("Press 1 to Create it \nPress 2 to Get Out\n")
        if int(desition) == 1:
            manager.create_new_category(category)
            print("Category created")
        else:
            print("Gracias")
# Remove rule by list of shieet
