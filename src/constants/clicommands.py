from ..models import Command
from ..constants.strings import *

# CLI commands that a user can provide
QUIT = Command(
    command="quit",
    aliases=["q", "stop", "exit"],
    short_desc=COMM_QUIT_SHORT_DESC,
    long_desc=COMM_QUIT_SHORT_DESC,
)
HELP = Command(
    command="help",
    long_desc=COMM_HELP_LONG_DESC,
)
SHOW_DIAGRAM = Command(
    command="show",
    short_desc=COMM_SHOW_SHORT_DESC,
    long_desc=COMM_SHOW_LONG_DESC,
)

# Command modifiers
MOD_HELP = "--help"

MOD_LIST = "--list"
MOD_LIST_ALT = "-l"
