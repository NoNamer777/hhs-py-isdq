"""
HHS Project ISDQ
@author Oscar Wellner, 21144192
"""
from os import chdir
from pathlib import Path


if __name__ == "__main__":
    # Get the location of the `main.py` file and change the working directory
    # for the application to the project root folder
    location = Path(__file__)
    chdir(location.parent)

    try:

    except KeyboardInterrupt:
        pass
