"""
BRAIN/dispatcher.py
-------------------
Routes commands to the correct NOVA module.
"""

from COMMANDS.apps import apps
from COMMANDS.web import google_search, youtube_search
from COMMANDS.time import get_time, get_date
from COMMANDS.weather import get_weather
from COMMANDS.system import system

class Dispatcher:

    def dispatch(self, command: str):

        command = command.lower().strip()

                # =================================
        # SYSTEM CONTROLS
        # =================================

        if command == "system lock":

            return system.lock()

        if command == "system restart":

            return system.restart()

        if command == "system shutdown":

            return system.shutdown()

        if command == "system cancel":

            return system.cancel_shutdown()

        # =================================
        # CLOSE APPLICATION
        # =================================

        if command.startswith("close "):

            app = command.replace(
                "close ",
                "",
                1
            ).strip()

            return apps.close(app)

        # =================================
        # OPEN APPLICATION
        # =================================

        if command.startswith("open "):

            app = command.replace(
                "open ",
                "",
                1
            ).strip()

            return apps.open(app)

        # =================================
        # GOOGLE SEARCH
        # =================================

        if command.startswith(
            "search google for "
        ):

            query = command.replace(
                "search google for ",
                "",
                1
            ).strip()

            return google_search(query)

        # =================================
        # YOUTUBE SEARCH
        # =================================

        if command.startswith(
            "search youtube for "
        ):

            query = command.replace(
                "search youtube for ",
                "",
                1
            ).strip()

            return youtube_search(query)

        # =================================
        # TIME
        # =================================

        if command in [
            "what time is it",
            "what is the time",
            "tell me the time"
        ]:

            return get_time()

        # =================================
        # DATE
        # =================================

        if command in [
            "what is todays date",
            "what is the date",
            "tell me the date"
        ]:

            return get_date()

        # =================================
        # WEATHER - DEFAULT LOCATION
        # =================================

        if command in [
            "whats the weather",
            "what is the weather",
            "how is the weather",
            "weather",
            "temperature",
            "forecast",
            "is it raining",
            "is it sunny",
            "is it cloudy"
        ]:

            return get_weather()

        # =================================
        # WEATHER - SPECIFIC CITY
        # =================================

        if command.startswith(
            "weather in "
        ):

            city = command[
                len("weather in "):
            ].strip()

            return get_weather(city)

        if command.startswith(
            "weather at "
        ):

            city = command[
                len("weather at "):
            ].strip()

            return get_weather(city)

        if command.startswith(
            "weather for "
        ):

            city = command[
                len("weather for "):
            ].strip()

            return get_weather(city)

        # =================================
        # WEATHER - NATURAL SENTENCES
        # =================================

        if command.startswith(
            "whats the weather in "
        ):

            city = command[
                len("whats the weather in "):
            ].strip()

            return get_weather(city)

        if command.startswith(
            "what is the weather in "
        ):

            city = command[
                len("what is the weather in "):
            ].strip()

            return get_weather(city)

        if command.startswith(
            "how is the weather in "
        ):

            city = command[
                len("how is the weather in "):
            ].strip()

            return get_weather(city)

        # =================================
        # VOLUME
        # =================================

        if command.startswith(
            "volume "
        ):

            return command

        # =================================
        # BRIGHTNESS
        # =================================

        if command.startswith(
            "brightness "
        ):

            return command

        # =================================
        # UNKNOWN COMMAND
        # =================================

        return False


# =====================================
# Create Dispatcher
# =====================================

dispatcher = Dispatcher()