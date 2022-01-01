"""
HHS Project ISDQ
@author Oscar Wellner, 21144192
"""
from os import chdir
from pathlib import Path

from src.constants import *

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

    process_input()


def is_valid_input(value: str) -> bool:
    return find_command(value) is not None


def find_command(value: str) -> Command or None:
    for comm in VALID_INPUTS:
        if comm.command != value and value not in comm.aliases:
            continue

        return comm

    return None


if __name__ == "__main__":
    # Get the location of the `main.py` file and change the working directory
    # for the application to the project root folder
    location = Path(__file__)
    chdir(location.parent)

    try:
        print(f"{APPLICATION_TITLE} {APPLICATION_VERSION}")

        process_input()

    except KeyboardInterrupt:
        pass
