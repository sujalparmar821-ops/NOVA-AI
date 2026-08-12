"""
BRAIN/dispatcher.py
-------------------
Routes commands to the correct NOVA module.
"""

import os

from COMMANDS.apps import apps
from COMMANDS.web import google_search, youtube_search, web
from COMMANDS.time import get_time, get_date
from COMMANDS.weather import get_weather
from COMMANDS.system import system
from COMMANDS.media import media
from COMMANDS.files import files
from COMMANDS.clipboard import clipboard
from COMMANDS.screenshot import screenshot
from COMMANDS.window import window
from COMMANDS.mouse import mouse


class Dispatcher:

    def dispatch(self, command: str):

        command = command.lower().strip()

        # =================================
        # FILE TYPE SEARCH
        # =================================

        if command.startswith("file type search "):

            extension = command.replace(
                "file type search ",
                "",
                1
            ).strip()

            if not extension:

                return (
                    "What type of file "
                    "should I search for?"
                )

            if not extension.startswith("."):

                extension = "." + extension

            print(
                f"🔎 Searching for {extension} files..."
            )

            results = files.search(
                "",
                extension=extension
            )

            if not results:

                print(
                    "❌ No matching files found."
                )

                return (
                    f"I couldn't find any "
                    f"{extension} files."
                )

            print(
                f"✅ Found {len(results)} "
                f"{extension} file"
                f"{'s' if len(results) != 1 else ''}."
            )

            for index, result in enumerate(
                results[:10],
                start=1
            ):

                print(
                    f"{index}. {result}"
                )

            return (
                f"I found {len(results)} "
                f"{extension} file"
                f"{'s' if len(results) != 1 else ''}."
            )

        # =================================
        # SMART FILE SEARCH
        # =================================

        if command.startswith("file search "):

            query = command.replace(
                "file search ",
                "",
                1
            ).strip()

            if not query:

                return (
                    "What file or folder "
                    "should I search for?"
                )

            print(
                f"🔎 Searching for: {query}"
            )

            results = files.search(
                query
            )

            if not results:

                print(
                    "❌ No matching files "
                    "or folders found."
                )

                return (
                    f"I couldn't find anything "
                    f"matching {query}."
                )

            print(
                f"✅ Found {len(results)} "
                f"result"
                f"{'s' if len(results) != 1 else ''}."
            )

            for index, result in enumerate(
                results[:10],
                start=1
            ):

                print(
                    f"{index}. {result}"
                )

            # ---------------------------------
            # SMART MATCH
            # ---------------------------------

            match = files.find_best_match(
                query,
                results
            )

            if not match:

                return (
                    f"I found some results for "
                    f"{query}, but I couldn't "
                    f"select a match."
                )

            # ---------------------------------
            # MULTIPLE EQUALLY GOOD RESULTS
            # ---------------------------------

            if match["status"] == "multiple":

                print(
                    "⚠️ Multiple equally good matches."
                )

                return (
                    f"I found {len(match['matches'])} "
                    f"equally good matches for "
                    f"{query}. I won't open one "
                    f"randomly."
                )

            # ---------------------------------
            # ONE CLEAR BEST MATCH
            # ---------------------------------

            best_path = match["path"]

            print(
                f"🎯 Best match: {best_path}"
            )

            opened = files.open_path(
                best_path
            )

            if opened:

                name = os.path.basename(
                    best_path
                )

                print(
                    f"📂 Opening: {name}"
                )

                return (
                    f"I found it and opened "
                    f"{name}."
                )

            return (
                f"I found the best match at "
                f"{best_path}, but I couldn't "
                f"open it."
            )

        # =================================
        # CLIPBOARD
        # =================================

        if command == "clipboard read":

            return clipboard.get_text()

        if command.startswith("clipboard write "):

            content = command.replace(
                "clipboard write ",
                "",
                1
            ).strip()

            return clipboard.set_text(
                content
            )

        if command == "clipboard clear":

            return clipboard.clear()

        if command == "clipboard search":

            query = clipboard.get_raw_text()

            if not query:

                return "Your clipboard is empty."

            print(
                f"🔎 Searching clipboard: {query}"
            )

            return google_search(query)

        # =================================
        # SCREENSHOT
        # =================================

        if command == "screenshot take":

            return screenshot.take()

        # =================================
        # WEB CONTROLS
        # =================================

        if command.startswith("google search "):

            query = command.replace(
                "google search ",
                "",
                1
            ).strip()

            return google_search(query)

        if command.startswith("youtube search "):

            query = command.replace(
                "youtube search ",
                "",
                1
            ).strip()

            return youtube_search(query)

        if command == "web open google":

            return web.open_google()

        if command == "web open youtube":

            return web.open_youtube()

        if command == "web open gmail":

            return web.open_gmail()

        if command == "web open github":

            return web.open_github()

        if command == "web open chatgpt":

            return web.open_chatgpt()

        # =================================
        # MEDIA
        # =================================

        if command == "media play pause":

            return media.play_pause()

        if command == "media next":

            return media.next_track()

        if command == "media previous":

            return media.previous_track()

        # =================================
        # SYSTEM
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
        # FOLDER CONTROLS
        # =================================

        if command.startswith("folder open "):

            folder = command.replace(
                "folder open ",
                "",
                1
            ).strip()

            return files.open_folder(
                folder
            )

        if command.startswith("folder create "):

            folder = command.replace(
                "folder create ",
                "",
                1
            ).strip()

            return files.create_folder(
                folder
            )

        # =================================
        # MOUSE CONTROLS
        # =================================  

                # ---------------------------------
        # MOVE TO SCREEN POSITION
        # ---------------------------------

        if command.startswith("mouse position "):

            position = command.replace(
                "mouse position ",
                "",
                1
            ).strip()

            return mouse.move_position(
                position
            )

        # ---------------------------------
        # MOVE MOUSE
        # ---------------------------------  



        if command.startswith("mouse move "):

            coordinates = command.replace(
                "mouse move ",
                "",
                1
            ).strip()

            parts = coordinates.split()

            if len(parts) != 2:

                return (
                    "Please provide "
                    "an X and Y coordinate."
                )

            x, y = parts

            return mouse.move(
                x,
                y
            )

        # ---------------------------------
        # LEFT CLICK
        # ---------------------------------

        if command == "mouse click":

            return mouse.click()

        # ---------------------------------
        # DOUBLE CLICK
        # ---------------------------------

        if command == "mouse double click":

            return mouse.double_click()

        # ---------------------------------
        # RIGHT CLICK
        # ---------------------------------

        if command == "mouse right click":

            return mouse.right_click()

        # ---------------------------------
        # SCROLL UP
        # ---------------------------------

        if command == "mouse scroll up":

            return mouse.scroll_up()

        # ---------------------------------
        # SCROLL DOWN
        # ---------------------------------

        if command == "mouse scroll down":

            return mouse.scroll_down()

        # =================================
        # CLOSE APPLICATION
        # =================================

        if command.startswith("close "):

            app = command.replace(
                "close ",
                "",
                1
            ).strip()

            return apps.close(
                app
            )

        # =================================
        # OPEN APPLICATION
        # =================================

        if command.startswith("open "):

            app = command.replace(
                "open ",
                "",
                1
            ).strip()

            return apps.open(
                app
            )

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
            "tell me the time",
            "whats the time"
        ]:

            return get_time()

        # =================================
        # DATE
        # =================================

        if command in [
            "what is todays date",
            "what is the date",
            "tell me the date",
            "whats the date",
            "whats todays date"
        ]:

            return get_date()

        # =================================
        # WEATHER
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
        # WEATHER — CITY
        # =================================

        if command.startswith("weather in "):

            city = command[
                len("weather in "):
            ].strip()

            return get_weather(city)

        if command.startswith("weather at "):

            city = command[
                len("weather at "):
            ].strip()

            return get_weather(city)

        if command.startswith("weather for "):

            city = command[
                len("weather for "):
            ].strip()

            return get_weather(city)

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

        if command.startswith("volume "):

            return command

        # =================================
        # BRIGHTNESS
        # =================================

        if command.startswith("brightness "):

            return command

        # =================================
        # WINDOW CONTROLS
        # =================================

        if command == "window minimize":

            return window.minimize()

        if command == "window maximize":

            return window.maximize()

        if command == "window close":

            return window.close()

        if command == "window show desktop":

            return window.show_desktop()

        # =================================
        # UNKNOWN COMMAND
        # =================================

        return False


# =====================================
# CREATE DISPATCHER
# =====================================

dispatcher = Dispatcher()