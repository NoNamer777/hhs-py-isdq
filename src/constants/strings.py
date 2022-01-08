APPLICATION_TITLE = "Data Modeling"
APPLICATION_VERSION = "v0.0.1"

UNKNOWN_COMMAND_EXCEPTION = "\nUnknown command '{}'. Type `help` for available commands"
INVALID_COMMAND_USE = "\nInvalid use of command '{}'. Type {} --help for command info"
INVALID_DIAGRAM_OPTION_EXCEPTION = "\nInvalid value for selecting a diagram. Should be a `1` or `2`"

COMM_HELP_SHORT_DESC = "Shows you this text."
COMM_QUIT_SHORT_DESC = "Closes the application."
COMM_SHOW_SHORT_DESC = "Shows you a diagram of your choice."

COMM_HELP_LONG_DESC = f"""
{APPLICATION_TITLE} {APPLICATION_VERSION}
This application allows you to choose between two diagrams to be shown.
The diagrams are create with help from the MatPlotLib.plt, and Numpy.
The data is extracted from the Game Paradise database provided by HHS and extracted into a CSV file with
help from the SSMS tool.

Commands available are:
- help
    {COMM_HELP_SHORT_DESC}
- quit
    {COMM_QUIT_SHORT_DESC}
- show
    {COMM_SHOW_SHORT_DESC}

For extra information about a command type the command in the terminal with `--help` appended to it."""

COMM_SHOW_LONG_DESC = f"""{COMM_SHOW_SHORT_DESC}

Enter the command with a number, either 1 or 2, to show diagram 1 or 2. When showing a diagram you'll be shown:
- a diagram
- a description of what the diagram is about
- description of the information about the x-axis and y-axis"""
