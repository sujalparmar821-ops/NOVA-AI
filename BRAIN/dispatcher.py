"""
BRAIN/dispatcher.py
-------------------
Routes commands to the correct module.
"""

from COMMANDS.apps import apps
from COMMANDS.web import google_search, youtube_search
from COMMANDS.time import get_time, get_date


class Dispatcher:

    def dispatch(self, command: str) -> bool:

        command = command.lower().strip()
        

        # Open applications
        if command.startswith("open "):
            app = command.replace("open ", "", 1).strip()
            return apps.open(app)

        # Google Search
        if command.startswith("search google for "):
            query = command.replace(
                "search google for ", "", 1
            ).strip()

            return google_search(query)

        # YouTube Search
        if command.startswith("search youtube for "):
            query = command.replace(
                "search youtube for ", "", 1
            ).strip()

            return youtube_search(query)

        # Time
        if command in [
            "what time is it",
            "what is the time",
            "tell me the time"
        ]:
             return get_time()

        # Date
        if command in [
            "what is today's date",
            "what is the date",
            "tell me the date"
        ]:
            return get_date()

        return False


dispatcher = Dispatcher()