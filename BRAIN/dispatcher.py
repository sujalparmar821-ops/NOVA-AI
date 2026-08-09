"""
BRAIN/dispatcher.py
-------------------
Routes parsed commands to the correct module.
"""

from COMMANDS.apps import apps
from COMMANDS.web import google_search, youtube_search
from COMMANDS.time import get_time, get_date
from COMMANDS.weather import get_weather
from COMMANDS.volume import volume
from COMMANDS.brightness import brightness
class Dispatcher:

    def dispatch(self, command: str):

        command = command.lower().strip()

        # -----------------------------
        # Open applications
        # -----------------------------
        if command.startswith("open "):

            app = command.replace(
                "open ",
                "",
                1
            ).strip()

            return apps.open(app)

        # -----------------------------
        # Google Search
        # -----------------------------
        if command.startswith("search google for "):

            query = command.replace(
                "search google for ",
                "",
                1
            ).strip()

            return google_search(query)

        # -----------------------------
        # YouTube Search
        # -----------------------------
        if command.startswith("search youtube for "):

            query = command.replace(
                "search youtube for ",
                "",
                1
            ).strip()

            return youtube_search(query)

        # -----------------------------
        # Time
        # -----------------------------
        if command in [
            "what time is it",
            "what is the time",
            "tell me the time"
        ]:

            return get_time()

        # -----------------------------
        # Date
        # -----------------------------
        if command in [
            "what is todays date",
            "what is the date",
            "tell me the date"
        ]:

            return get_date()

                # -----------------------------
        # Brightness
        # -----------------------------

        if command == "brightness get":

            current = brightness.get_brightness()

            if current is None:
                return "I couldn't read the screen brightness."

            return f"Current brightness is {current} percent."

        if command == "brightness increase":

            return brightness.increase()

        if command == "brightness decrease":

            return brightness.decrease()

        if command.startswith("brightness set "):

            percentage = command.replace(
                "brightness set ",
                "",
                1
            ).strip()

            return brightness.set_brightness(
                int(percentage)
            )


                # -----------------------------
        # Volume
        # -----------------------------

        if command == "volume get":

            return f"Current volume is {volume.get_volume()} percent."

        if command == "volume increase":

            return volume.increase()

        if command == "volume decrease":

            return volume.decrease()

        if command == "volume mute":

            return volume.mute()

        if command == "volume unmute":

            return volume.unmute()

        if command.startswith("volume set "):

            percentage = command.replace(
                "volume set ",
                "",
                1
            ).strip()

            return volume.set_volume(
                int(percentage)
            )

        # -----------------------------
        # Weather - default location
        # -----------------------------
        if command == "weather":

            return get_weather()

        # -----------------------------
        # Weather - specific city
        # -----------------------------
        if command.startswith("weather in "):

            city = command.replace(
                "weather in ",
                "",
                1
            ).strip()

            if city:

                return get_weather(city)

            return get_weather()

        # -----------------------------
        # Unknown command
        # -----------------------------
        return False


# Create dispatcher
dispatcher = Dispatcher()