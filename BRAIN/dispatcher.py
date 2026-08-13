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
from COMMANDS.keyboard import keyboard
from COMMANDS.volume import volume
from COMMANDS.brightness import brightness


class Dispatcher:

    def dispatch(self, command: str):

        if not command:
            return False

        command = command.lower().strip()

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

        if command.startswith("window focus "):

            app_name = command.replace(
                "window focus ",
                "",
                1
            ).strip()

            if not app_name:
                return (
                    "Please tell me which "
                    "application to focus."
                )

            return window.focus_app(
                app_name
            )

        if command == "window switch next":
            return window.switch_next()

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
                f"🔎 Searching for "
                f"{extension} files..."
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

            if match["status"] == "multiple":

                return (
                    f"I found "
                    f"{len(match['matches'])} "
                    f"equally good matches for "
                    f"{query}. I won't open one "
                    f"randomly."
                )

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

            if not content:
                return "There is nothing to copy."

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
        # WEB
        # =================================

        if command.startswith("google search "):

            query = command.replace(
                "google search ",
                "",
                1
            ).strip()

            if not query:
                return "What should I search for?"

            return google_search(query)

        if command.startswith("youtube search "):

            query = command.replace(
                "youtube search ",
                "",
                1
            ).strip()

            if not query:
                return "What should I search for?"

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
        # FOLDERS
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
        # MOUSE
        # =================================

        if command.startswith("mouse position "):

            position = command.replace(
                "mouse position ",
                "",
                1
            ).strip()

            return mouse.move_position(
                position
            )

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

        if command == "mouse click":
            return mouse.click()

        if command == "mouse double click":
            return mouse.double_click()

        if command == "mouse right click":
            return mouse.right_click()

        if command == "mouse scroll up":
            return mouse.scroll_up()

        if command == "mouse scroll down":
            return mouse.scroll_down()

        # =================================
        # KEYBOARD
        # =================================

        if command.startswith("keyboard press "):

            key = command.replace(
                "keyboard press ",
                "",
                1
            ).strip()

            if not key:
                return (
                    "Please tell me which "
                    "key to press."
                )

            return keyboard.press(key)

        if command.startswith("keyboard hotkey "):

            keys = command.replace(
                "keyboard hotkey ",
                "",
                1
            ).strip()

            if not keys:
                return (
                    "Please tell me which "
                    "keys to press."
                )

            return keyboard.hotkey(
                *keys.split()
            )

        if command.startswith("keyboard type "):

            content = command.replace(
                "keyboard type ",
                "",
                1
            ).strip()

            if not content:
                return (
                    "Please tell me what "
                    "you want me to type."
                )

            return keyboard.type_text(
                content
            )

        # =================================
        # APPLICATIONS
        # =================================

        if command.startswith("close "):

            app = command.replace(
                "close ",
                "",
                1
            ).strip()

            if not app:
                return "Which application should I close?"

            return apps.close(app)

        if command.startswith("open "):

            app = command.replace(
                "open ",
                "",
                1
            ).strip()

            if not app:
                return "Which application should I open?"

            return apps.open(app)

        # =================================
        # TIME
        # =================================

        if command in [
            "what time is it",
            "what is the time",
            "tell me the time",
            "whats the time",
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
            "whats todays date",
        ]:

            return get_date()

        # =================================
        # WEATHER
        # =================================

        if command in [
            "weather",
            "whats the weather",
            "what is the weather",
            "how is the weather",
            "temperature",
            "forecast",
            "is it raining",
            "is it sunny",
            "is it cloudy",
        ]:

            return get_weather()

        if command.startswith("weather in "):

            city = command[
                len("weather in "):
            ].strip()

            if not city:
                return get_weather()

            return get_weather(city)

        if command.startswith("weather at "):

            city = command[
                len("weather at "):
            ].strip()

            if not city:
                return get_weather()

            return get_weather(city)

        if command.startswith("weather for "):

            city = command[
                len("weather for "):
            ].strip()

            if not city:
                return get_weather()

            return get_weather(city)

        # =================================
        # VOLUME
        # =================================

        if command == "volume get":

            current = volume.get_volume()

            if current is None:
                return "I couldn't read the current volume."

            return (
                f"Your volume is currently "
                f"{current} percent."
            )

        if command.startswith("volume set "):

            percentage = command.replace(
                "volume set ",
                "",
                1
            ).strip()

            if not percentage.isdigit():

                return (
                    "Please give me a volume "
                    "percentage between 0 and 100."
                )

            percentage = int(percentage)

            if percentage < 0 or percentage > 100:

                return (
                    "Please choose a volume "
                    "between 0 and 100 percent."
                )

            return volume.set_volume(
                percentage
            )

        if command == "volume increase":
            return volume.increase()

        if command == "volume decrease":
            return volume.decrease()

        if command == "volume mute":
            return volume.mute()

        if command == "volume unmute":
            return volume.unmute()

        # =================================
        # BRIGHTNESS
        # =================================

        if command == "brightness get":

            current = brightness.get_brightness()

            if current is None:
                return (
                    "I couldn't read the "
                    "current brightness."
                )

            return (
                f"Your brightness is currently "
                f"{current} percent."
            )

        if command.startswith("brightness set "):

            percentage = command.replace(
                "brightness set ",
                "",
                1
            ).strip()

            if not percentage.isdigit():

                return (
                    "Please give me a brightness "
                    "percentage between 0 and 100."
                )

            percentage = int(percentage)

            if percentage < 0 or percentage > 100:

                return (
                    "Please choose a brightness "
                    "between 0 and 100 percent."
                )

            return brightness.set_brightness(
                percentage
            )

        if command == "brightness increase":
            return brightness.increase()

        if command == "brightness decrease":
            return brightness.decrease()

        # =================================
        # UNKNOWN
        # =================================

        return False


# =====================================
# CREATE DISPATCHER
# =====================================

dispatcher = Dispatcher()