"""
HHS Project ISDQ
@author Oscar Wellner, 21144192
"""
import matplotlib.pyplot as plt
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
    elif comm == SHOW_DIAGRAM:
        show_diagram(input_value.split(" ")[1])

    process_input()


def show_diagram(diagram_number: str) -> None:
    diagram_nr = str_to_int(diagram_number)

    if diagram_nr > 2 or diagram_nr < 1:
        print(INVALID_DIAGRAM_OPTION_EXCEPTION)

    if diagram_nr == 1:
        print(DIAGRAM_1_DESCRIPTION)
        plt.bar(DIAGRAM_1_DATA_X, DIAGRAM_1_DATA_Y)
        plt.xticks(DIAGRAM_1_DATA_X, DIAGRAM_1_DATA_X, rotation=10)
        plt.title(DIAGRAM_1_TITLE)
        plt.show()
    elif diagram_nr == 2:
        print(DIAGRAM_2_DESCRIPTION)
        plt.pie(DIAGRAM_2_DATA_Y, labels=DIAGRAM_2_DATA_Y)
        plt.title(DIAGRAM_2_TITLE)
        plt.legend(DIAGRAM_2_DATA_X, bbox_to_anchor=(1.3, 0.1))
        plt.show()
        pass


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
