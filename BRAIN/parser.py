"""
BRAIN/parser.py
----------------
Converts natural language into executable commands.
"""

import re


class Parser:

    def parse(self, text: str) -> str:

        text = text.lower().strip()

        # =================================
        # REMOVE PUNCTUATION
        # =================================

        text = re.sub(
            r"[^\w\s]",
            "",
            text
        )

        # =================================
        # COMMON FILLER WORDS
        # =================================

        fillers = [
            "please",
            "can you",
            "could you",
            "would you",
            "for me",
            "i want to",
            "i would like to",
            "nova",
        ]

        for filler in fillers:
            text = text.replace(
                filler,
                ""
            )

        text = " ".join(text.split())

        # =================================
        # GOOGLE SEARCH
        # =================================

        google_patterns = [
            r"^search google for (.+)$",
            r"^google search for (.+)$",
            r"^search google (.+)$",
            r"^google (.+)$",
        ]

        for pattern in google_patterns:

            match = re.match(
                pattern,
                text
            )

            if match:

                query = match.group(1).strip()

                if query:
                    return f"google search {query}"

        # =================================
        # YOUTUBE SEARCH
        # =================================

        youtube_patterns = [
            r"^search youtube for (.+)$",
            r"^youtube search for (.+)$",
            r"^search youtube (.+)$",
            r"^youtube (.+)$",
        ]

        for pattern in youtube_patterns:

            match = re.match(
                pattern,
                text
            )

            if match:

                query = match.group(1).strip()

                if query:
                    return f"youtube search {query}"

        # =================================
        # OPEN WEBSITES
        # =================================

        website_commands = {

            "open google":
                "web open google",

            "launch google":
                "web open google",

            "start google":
                "web open google",

            "open youtube":
                "web open youtube",

            "launch youtube":
                "web open youtube",

            "start youtube":
                "web open youtube",

            "open gmail":
                "web open gmail",

            "launch gmail":
                "web open gmail",

            "start gmail":
                "web open gmail",

            "open email":
                "web open gmail",

            "open my email":
                "web open gmail",

            "open github":
                "web open github",

            "launch github":
                "web open github",

            "start github":
                "web open github",

            "open chatgpt":
                "web open chatgpt",

            "open chat gpt":
                "web open chatgpt",

            "launch chatgpt":
                "web open chatgpt",

            "launch chat gpt":
                "web open chatgpt",

            "start chatgpt":
                "web open chatgpt",
        }

        if text in website_commands:
            return website_commands[text]

        # =================================
        # FILE TYPE SEARCH
        # =================================

        file_type_aliases = {

            "pdf": "pdf",
            "pdfs": "pdf",

            "png": "png",
            "pngs": "png",

            "jpg": "jpg",
            "jpgs": "jpg",

            "jpeg": "jpeg",
            "jpegs": "jpeg",

            "gif": "gif",
            "gifs": "gif",

            "webp": "webp",

            "python": "py",
            "python file": "py",
            "python files": "py",
            "py": "py",

            "text": "txt",
            "text file": "txt",
            "text files": "txt",
            "txt": "txt",

            "word": "docx",
            "word file": "docx",
            "word files": "docx",
            "docx": "docx",

            "excel": "xlsx",
            "excel file": "xlsx",
            "excel files": "xlsx",
            "xlsx": "xlsx",

            "powerpoint": "pptx",
            "powerpoint file": "pptx",
            "powerpoint files": "pptx",
            "pptx": "pptx",

            "zip": "zip",
            "zips": "zip",

            "rar": "rar",
            "rars": "rar",
        }

        type_match = re.match(
            r"^(?:find|search for|search)"
            r"\s+(?:all\s+)?(.+?)"
            r"(?:\s+files?)?$",
            text
        )

        if type_match:

            requested_type = (
                type_match.group(1).strip()
            )

            if requested_type in file_type_aliases:

                extension = file_type_aliases[
                    requested_type
                ]

                return (
                    f"file type search "
                    f"{extension}"
                )

        # =================================
        # COMMON WINDOWS FOLDERS
        # =================================

        folders = {

            "desktop": [
                "desktop",
                "my desktop",
                "desktop folder",
                "my desktop folder",
            ],

            "downloads": [
                "download",
                "downloads",
                "my download",
                "my downloads",
                "download folder",
                "downloads folder",
                "my download folder",
                "my downloads folder",
            ],

            "documents": [
                "document",
                "documents",
                "my document",
                "my documents",
                "document folder",
                "documents folder",
                "my document folder",
                "my documents folder",
            ],

            "pictures": [
                "picture",
                "pictures",
                "my picture",
                "my pictures",
                "picture folder",
                "pictures folder",
                "my picture folder",
                "my pictures folder",
            ],

            "videos": [
                "video",
                "videos",
                "my video",
                "my videos",
                "video folder",
                "videos folder",
                "my video folder",
                "my videos folder",
            ],

            "music": [
                "music",
                "my music",
                "music folder",
                "my music folder",
            ],
        }

        # =================================
        # OPEN COMMON FOLDER
        # =================================

        open_folder_actions = [
            "open",
            "launch",
            "start",
            "show",
            "go to",
        ]

        for action in open_folder_actions:

            for folder_name, aliases in folders.items():

                for alias in aliases:

                    if text == f"{action} {alias}":

                        return (
                            f"folder open "
                            f"{folder_name}"
                        )

        # =================================
        # CREATE FOLDER
        # =================================

        create_match = re.match(
            r"^(?:create|make|new)"
            r"\s+(?:a\s+)?folder"
            r"\s+(?:called|named)\s+(.+)$",
            text
        )

        if create_match:

            folder_name = (
                create_match.group(1).strip()
            )

            return (
                f"folder create "
                f"{folder_name}"
            )

        # =================================
        # WINDOW CONTROLS
        # =================================

        minimize_commands = [
            "minimize",
            "minimise",
            "minimize this",
            "minimise this",
            "minimize window",
            "minimise window",
            "minimize the window",
            "minimise the window",
            "minimize this window",
            "minimise this window",
            "minimize current window",
            "minimise current window",
            "minimize the current window",
            "minimise the current window",
            "window minimize",
            "window minimise",
        ]

        if text in minimize_commands:
            return "window minimize"

        maximize_commands = [
            "maximize",
            "maximise",
            "maximize this",
            "maximise this",
            "maximize window",
            "maximise window",
            "maximize the window",
            "maximise the window",
            "maximize this window",
            "maximise this window",
            "maximize current window",
            "maximise current window",
            "maximize the current window",
            "maximise the current window",
            "window maximize",
            "window maximise",
        ]

        if text in maximize_commands:
            return "window maximize"

        close_commands = [
            "close",
            "close this",
            "close window",
            "close the window",
            "close this window",
            "close current window",
            "close the current window",
            "window close",
        ]

        if text in close_commands:
            return "window close"

        show_desktop_commands = [
            "show desktop",
            "show my desktop",
            "show the desktop",
            "go to desktop",
            "go to my desktop",
            "display desktop",
            "display my desktop",
            "minimize everything",
            "show me the desktop",
            "window show desktop",
        ]

        if text in show_desktop_commands:
            return "window show desktop"

        # =================================
        # APPLICATION FOCUS
        # =================================

        focus_match = re.match(
            r"^(?:switch to|focus|bring)"
            r"\s+(.+?)"
            r"(?:\s+to the front)?$",
            text
        )

        if focus_match:

            app_name = (
                focus_match.group(1).strip()
            )

            if app_name:
                return (
                    f"window focus "
                    f"{app_name}"
                )

        # =================================
        # NEXT WINDOW
        # =================================

        if text in [
            "switch window",
            "switch windows",
            "switch to next window",
            "switch to the next window",
            "next window",
            "alt tab",
            "switch application",
            "switch applications",
            "switch app",
            "switch apps",
        ]:

            return "window switch next"

        # =================================
        # CLIPBOARD
        # =================================

        if text in [
            "search my clipboard",
            "search the clipboard",
            "search whats in my clipboard",
            "search what is in my clipboard",
            "google my clipboard",
            "search clipboard",
        ]:

            return "clipboard search"

        clipboard_write_match = re.match(
            r"^(?:copy|put|save)"
            r"\s+(.+?)\s+"
            r"(?:to|into)\s+"
            r"(?:my\s+|the\s+)?clipboard$",
            text
        )

        if clipboard_write_match:

            content = (
                clipboard_write_match.group(1).strip()
            )

            if content:
                return (
                    f"clipboard write "
                    f"{content}"
                )

        if text in [
            "clear my clipboard",
            "clear the clipboard",
            "empty my clipboard",
            "empty the clipboard",
            "delete my clipboard",
            "delete the clipboard",
        ]:

            return "clipboard clear"

        if text in [
            "read my clipboard",
            "read the clipboard",
            "check my clipboard",
            "check the clipboard",
            "what is on my clipboard",
            "whats on my clipboard",
            "show me my clipboard",
            "show my clipboard",
            "tell me whats on my clipboard",
            "tell me what is on my clipboard",
        ]:

            return "clipboard read"

        # =================================
        # SCREENSHOT
        # =================================

        if text in [
            "take a screenshot",
            "take screenshot",
            "capture the screen",
            "capture screen",
            "capture my screen",
            "screenshot",
            "take a screen shot",
            "take screen shot",
        ]:

            return "screenshot take"

        # =================================
        # MEDIA
        # =================================

        if text in [
            "play",
            "play music",
            "play the music",
            "play media",
            "play the media",
            "resume",
            "resume music",
            "resume the music",
            "resume media",
            "resume the media",
            "pause",
            "pause music",
            "pause the music",
            "pause media",
            "pause the media",
            "pause playback",
            "pause the playback",
            "stop music",
            "stop the music",
        ]:

            return "media play pause"

        if text in [
            "next",
            "next song",
            "next track",
            "skip",
            "skip song",
            "skip track",
            "skip this song",
            "next music",
        ]:

            return "media next"

        if text in [
            "previous",
            "previous song",
            "previous track",
            "go back",
            "go to previous",
            "previous music",
            "last song",
            "last track",
        ]:

            return "media previous"

        # =================================
        # SYSTEM
        # =================================

        if text in [
            "cancel shutdown",
            "cancel the shutdown",
            "cancel restart",
            "cancel the restart",
            "abort shutdown",
            "abort the shutdown",
            "abort restart",
            "abort the restart",
            "stop shutdown",
            "stop the shutdown",
            "stop restart",
            "stop the restart",
        ]:

            return "system cancel"

        if text in [
            "lock my computer",
            "lock the computer",
            "lock my pc",
            "lock the pc",
            "lock computer",
            "lock pc",
        ]:

            return "system lock"

        if text in [
            "restart my computer",
            "restart the computer",
            "restart my pc",
            "restart the pc",
            "restart computer",
            "restart pc",
        ]:

            return "system restart"

        if text in [
            "shut down my computer",
            "shutdown my computer",
            "shut down the computer",
            "shutdown the computer",
            "shut down my pc",
            "shutdown my pc",
            "shut down the pc",
            "shutdown the pc",
            "shut down computer",
            "shutdown computer",
        ]:

            return "system shutdown"

        # =================================
        # MOUSE
        # =================================

        if text.startswith("move the mouse to "):

            position = text[
                len("move the mouse to "):
            ].strip()

            if position in [
                "centre",
                "center",
                "middle",
                "centre of the screen",
                "center of the screen",
                "middle of the screen",
            ]:

                return "mouse position centre"

        if text.startswith("move mouse to "):

            position = text[
                len("move mouse to "):
            ].strip()

            if position in [
                "centre",
                "center",
                "middle",
                "centre of the screen",
                "center of the screen",
                "middle of the screen",
            ]:

                return "mouse position centre"

        mouse_move_match = re.match(
            r"^move (?:the )?mouse"
            r"(?: to)?\s+(\d+)\s+(\d+)$",
            text
        )

        if mouse_move_match:

            x = mouse_move_match.group(1)
            y = mouse_move_match.group(2)

            return (
                f"mouse move "
                f"{x} {y}"
            )

        if text in [
            "click",
            "mouse click",
            "left click",
            "left mouse click",
            "click the mouse",
        ]:

            return "mouse click"

        if text in [
            "double click",
            "doubleclick",
            "mouse double click",
            "double click the mouse",
            "double click with the mouse",
        ]:

            return "mouse double click"

        if text in [
            "right click",
            "mouse right click",
            "right click the mouse",
            "right click with the mouse",
        ]:

            return "mouse right click"

        if text in [
            "scroll up",
            "scroll upwards",
            "mouse scroll up",
            "scroll up the page",
            "scroll upward",
        ]:

            return "mouse scroll up"

        if text in [
            "scroll down",
            "scroll downwards",
            "mouse scroll down",
            "scroll down the page",
            "scroll downward",
        ]:

            return "mouse scroll down"

        # =================================
        # KEYBOARD
        # =================================

        keyboard_keys = {

            "enter": "enter",
            "return": "enter",

            "escape": "esc",
            "esc": "esc",

            "tab": "tab",

            "space": "space",
            "spacebar": "space",

            "backspace": "backspace",
            "back space": "backspace",

            "delete": "delete",
            "del": "delete",

            "up": "up",
            "up arrow": "up",

            "down": "down",
            "down arrow": "down",

            "left": "left",
            "left arrow": "left",

            "right": "right",
            "right arrow": "right",

            "home": "home",
            "end": "end",

            "page up": "pageup",
            "page down": "pagedown",

            "insert": "insert",

            "f1": "f1",
            "f2": "f2",
            "f3": "f3",
            "f4": "f4",
            "f5": "f5",
            "f6": "f6",
            "f7": "f7",
            "f8": "f8",
            "f9": "f9",
            "f10": "f10",
            "f11": "f11",
            "f12": "f12",
        }

        hotkeys = {

            "ctrl c": ["ctrl", "c"],
            "control c": ["ctrl", "c"],

            "ctrl v": ["ctrl", "v"],
            "control v": ["ctrl", "v"],

            "ctrl x": ["ctrl", "x"],
            "control x": ["ctrl", "x"],

            "ctrl a": ["ctrl", "a"],
            "control a": ["ctrl", "a"],

            "ctrl z": ["ctrl", "z"],
            "control z": ["ctrl", "z"],

            "ctrl s": ["ctrl", "s"],
            "control s": ["ctrl", "s"],

            "ctrl f": ["ctrl", "f"],
            "control f": ["ctrl", "f"],

            "alt tab": ["alt", "tab"],
            "alt f4": ["alt", "f4"],

            "ctrl shift esc": [
                "ctrl",
                "shift",
                "esc",
            ],

            "control shift escape": [
                "ctrl",
                "shift",
                "esc",
            ],
        }

        if text.startswith("press "):

            key = text[
                len("press "):
            ].strip()

            if key in hotkeys:
                return (
                    "keyboard hotkey "
                    + " ".join(hotkeys[key])
                )

            if key in keyboard_keys:
                return (
                    "keyboard press "
                    + keyboard_keys[key]
                )

        if text.startswith("press the "):

            key = text[
                len("press the "):
            ].strip()

            if key in hotkeys:
                return (
                    "keyboard hotkey "
                    + " ".join(hotkeys[key])
                )

            if key in keyboard_keys:
                return (
                    "keyboard press "
                    + keyboard_keys[key]
                )

        # =================================
        # BRIGHTNESS
        # =================================

        brightness_match = re.search(
            r"(?:brightness|screen brightness|screen)"
            r"\s+(?:to|at)?\s*(\d+)"
            r"\s*(?:percent|%)?",
            text
        )

        if brightness_match:

            percentage = brightness_match.group(1)

            return (
                f"brightness set "
                f"{percentage}"
            )

        if any(
            phrase in text
            for phrase in [
                "increase brightness",
                "increase the brightness",
                "raise brightness",
                "raise the brightness",
                "make it brighter",
                "make the screen brighter",
                "brighter",
                "brightness up",
                "brightness higher",
                "screen brighter",
            ]
        ):

            return "brightness increase"

        if any(
            phrase in text
            for phrase in [
                "decrease brightness",
                "decrease the brightness",
                "lower brightness",
                "lower the brightness",
                "make it dimmer",
                "make the screen dimmer",
                "dimmer",
                "brightness down",
                "brightness lower",
                "screen dimmer",
            ]
        ):

            return "brightness decrease"

        if text in [
            "what is my brightness",
            "what is the brightness",
            "brightness",
            "check brightness",
            "check the brightness",
        ]:

            return "brightness get"

        # =================================
        # VOLUME
        # =================================

        volume_match = re.search(
            r"(?:volume|sound|audio)"
            r"\s+(?:to|at)?\s*(\d+)"
            r"\s*(?:percent|%)?",
            text
        )

        if volume_match:

            percentage = volume_match.group(1)

            return (
                f"volume set "
                f"{percentage}"
            )

        if text in [
            "mute",
            "mute volume",
            "mute sound",
            "mute audio",
        ]:

            return "volume mute"

        if text in [
            "unmute",
            "unmute volume",
            "unmute sound",
            "unmute audio",
        ]:

            return "volume unmute"

        if any(
            phrase in text
            for phrase in [
                "increase volume",
                "increase the volume",
                "raise volume",
                "raise the volume",
                "make it louder",
                "make the sound louder",
                "volume up",
                "volume higher",
                "louder",
                "sound up",
            ]
        ):

            return "volume increase"

        if any(
            phrase in text
            for phrase in [
                "decrease volume",
                "decrease the volume",
                "lower volume",
                "lower the volume",
                "make it quieter",
                "make the sound quieter",
                "volume down",
                "volume lower",
                "quieter",
                "sound down",
            ]
        ):

            return "volume decrease"

        if text in [
            "what is my volume",
            "what is the volume",
            "check volume",
            "check the volume",
            "volume",
            "how loud is it",
        ]:

            return "volume get"

        # =================================
        # WEATHER
        # =================================

        weather_words = [
            "weather",
            "temperature",
            "rain",
            "raining",
            "rainfall",
            "forecast",
            "sunny",
            "cloudy",
            "storm",
            "storms",
            "snow",
            "snowing",
            "hot",
            "cold",
        ]

        if any(
            word in text.split()
            for word in weather_words
        ):

            city = self.extract_city(text)

            if city:
                return f"weather in {city}"

            return "weather"

        # =================================
        # TYPE TEXT
        # =================================

        if text.startswith("type "):

            content = text[
                len("type "):
            ].strip()

            if content:
                return (
                    "keyboard type "
                    + content
                )

        # =================================
        # OPEN APPLICATION
        # =================================

        if text.startswith("open "):

            app = text[
                len("open "):
            ].strip()

            if app:
                return f"open {app}"

        # =================================
        # CLOSE APPLICATION
        # =================================

        if text.startswith("close "):

            app = text[
                len("close "):
            ].strip()

            if app:
                return f"close {app}"

        # =================================
        # GENERIC FILE SEARCH
        # =================================

        search_match = re.match(
            r"^(?:find|search for|search)"
            r"\s+(?:my\s+)?(.+)$",
            text
        )

        if search_match:

            query = (
                search_match.group(1).strip()
            )

            if query not in [
                "google",
                "youtube",
                "google for",
                "youtube for",
            ]:

                return f"file search {query}"

        # =================================
        # TIME
        # =================================

        if text in [
            "what time is it",
            "what is the time",
            "tell me the time",
            "whats the time",
        ]:

            return "what time is it"

        # =================================
        # DATE
        # =================================

        if text in [
            "what is todays date",
            "what is the date",
            "tell me the date",
            "whats the date",
            "whats todays date",
        ]:

            return "what is todays date"

        # =================================
        # RETURN CLEANED TEXT
        # =================================

        return text

    # =====================================
    # EXTRACT CITY
    # =====================================

    def extract_city(self, text):

        patterns = [
            r"\bin\s+([a-zA-Z\s]+)$",
            r"\bat\s+([a-zA-Z\s]+)$",
            r"\bfor\s+([a-zA-Z\s]+)$",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text
            )

            if match:

                city = (
                    match.group(1).strip()
                )

                city = re.sub(
                    r"\b(today|now|tonight|tomorrow)\b",
                    "",
                    city
                ).strip()

                if city:
                    return city

        return None


# =====================================
# CREATE PARSER
# =====================================

parser = Parser()