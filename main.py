import click
from commands.general_commands import show_themes
from commands.rules_commands import add_rules, search_rules
from filemanager import FileModificationManager

PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial",
}


@click.group()
def mycommands():
    pass


def hello():
    click.echo(click.style(f" Hello Pablo! ", bg='blue', fg='white'))
    click.echo(click.style(
        f" Aquí podrás realizar diversas acciones simplemente escribiendo los números del 0 al 9. ", bg='green'))
    click.echo(click.style(
        f"Para seleccionar una opción, simplemente escribe el número correspondiente y presiona enter.", bg='green'))
    click.echo(click.style(
        f"Presiona 1 para ver todas las categorias", bg='blue'))
    click.echo(click.style(
        f"Presiona 2 para aladir alguna categoria", bg='blue'))
    click.echo(click.style(
        f"Presiona 3 para ver las reglas", bg='blue'))
    click.echo(click.style(
        f"Presiona cualquier otro numero para salir", bg='blue'))
    value = click.prompt('Please enter a valid integer', type=int)
    return value

# @click.command()
# @click.argument("priority", type=click.Choice(PRIORITIES.keys()), default=PRIORITIES["m"])
# @click.argument("todofile", type=click.Path(exists=False), required=0)
# @click.option("-n", prompt="Enter the todo name", help="The name f the todo item")
# @click.option("-d", prompt="Describe the todo", help="The description of the todo item")
# def add_todo(name, description, priority, todofile):
#     filename = todofile if todofile is not None else "mytodos.txt"
#     with open(filename, "a+") as f:
#         f.write(f"{name}:{description} [Priority: {PRIORITIES[priority]}]")


mycommands.add_command(search_rules)
mycommands.add_command(add_rules)
mycommands.add_command(show_themes)

if __name__ == "__main__":
    result = hello()
    match result:
        case 0:
            click.echo("Adios")
            exit
        case 1:
            mycommands.invoke(show_themes())
        case 2:
            mycommands.invoke(add_rules())
        case 3:
            mycommands.invoke(search_rules())
        case 4:
            exit
        case 5:
            exit
        case 6:
            exit
        case 7:
            exit
        case 8:
            exit
        case 9:
            exit

    # mycommands.invoke(show_themes)
