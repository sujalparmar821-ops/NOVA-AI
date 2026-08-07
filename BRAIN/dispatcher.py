"""
BRAIN/dispatcher.py
-------------------
Routes commands to the correct module.
"""

from COMMANDS.apps import apps
from COMMANDS.web import google_search, youtube_search


class Dispatcher:

    def dispatch(self, command: str) -> bool:

        command = command.lower().strip()

        # Open applications
        if command.startswith("open "):
            app = command.replace("open ", "", 1).strip()
            return apps.open(app)

        # Google Search
        if command.startswith("search google for "):
            query = command.replace("search google for ", "", 1).strip()
            return google_search(query)

        # YouTube Search
        if command.startswith("search youtube for "):
            query = command.replace("search youtube for ", "", 1).strip()
            return youtube_search(query)

        return False


dispatcher = Dispatcher()