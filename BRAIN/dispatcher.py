"""
BRAIN/dispatcher.py
-------------------
Routes commands to the correct module.
"""

from COMMANDS.apps import open_app


class Dispatcher:

    def dispatch(self, command: str) -> bool:
        """
        Returns True if a command was executed.
        """

        command = command.lower().strip()

        if open_app(command):
            return True

        return False


dispatcher = Dispatcher()