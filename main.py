"""
HHS Project ISDQ
@author Oscar Wellner, 21144192
"""
from os import chdir
from pathlib import Path

from src.constants import *
from src.models import Diagram

VALID_INPUTS = tuple([QUIT, HELP, SHOW_DIAGRAM])


def process_input() -> None:
    input_value = input().lower()

    if not is_valid_input(input_value.split(" ")[0]):
        print(UNKNOWN_COMMAND_EXCEPTION.format(input_value, MOD_HELP))
        process_input()
        return

    comm = find_command(input_value.split(" ")[0])

    if comm.command == HELP.command:
        # Provide short application description
        print(comm.long_desc)

    if input_value.find(MOD_HELP) > -1:
        # Provide full description of command
        print(f"{comm.long_desc}\n")

    elif comm == QUIT:
        return
    elif comm == SHOW_DIAGRAM:
        show_diagram(input_value.split(" ")[1])

    process_input()


def show_diagram(diagram_number: str) -> None:
    diagram_nr = str_to_int(diagram_number)

    if diagram_nr > len(DIAGRAMS) or diagram_nr < 1:
        print(INVALID_DIAGRAM_OPTION_EXCEPTION)

    for idx, diagram in enumerate(DIAGRAMS):
        if idx + 1 != diagram_nr:
            continue

        diagram.show()

def is_valid_input(value: str) -> bool:
    return find_command(value) is not None


def find_command(value: str) -> Command or None:
    for comm in VALID_INPUTS:
        if comm.command != value and value not in comm.aliases:
            continue

        return comm

    return None


def str_to_int(value: str) -> int:
    try:
        return int(value, base=10)

    except ValueError:
        return 0


if __name__ == "__main__":
    # Get the location of the `main.py` file and change the working directory
    # for the application to the project root folder
    location = Path(__file__)
    chdir(location.parent)

    try:
        print(f"{APPLICATION_TITLE} {APPLICATION_VERSION}\n")

        process_input()

    except KeyboardInterrupt:
        pass
