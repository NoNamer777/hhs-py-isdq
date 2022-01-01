KEY_COMMAND_COMMAND = "command"
KEY_COMMAND_ALIASES = "aliases"
KEY_COMMAND_SHORT_DESC = "short_desc"
KEY_COMMAND_LONG_DESC = "long_desc"


class Command:
    def __init__(self, **kwargs):
        self._command = kwargs.get(KEY_COMMAND_COMMAND)
        self._aliases = kwargs.get(KEY_COMMAND_ALIASES) if KEY_COMMAND_ALIASES in kwargs.keys() else []
        self._short_desc = kwargs.get(KEY_COMMAND_SHORT_DESC)
        self._long_desc = kwargs.get(KEY_COMMAND_LONG_DESC)

    # GETTERS / SETTERS

    @property
    def command(self) -> str:
        return self._command

    @property
    def aliases(self) -> set[str]:
        return self._aliases

    @property
    def short_desc(self) -> str:
        return self._short_desc

    @property
    def long_desc(self) -> str:
        return self._long_desc
