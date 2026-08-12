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
        ]

        for word in fillers:

            text = text.replace(
                word,
                ""
            )

        text = " ".join(
            text.split()
        )

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
            r"^(?:find|search for|search)\s+"
            r"(?:all\s+)?(.+?)"
            r"(?:\s+files?)?$",
            text
        )

        if type_match:

            requested_type = (
                type_match.group(1)
                .strip()
            )

            if requested_type in file_type_aliases:

                extension = file_type_aliases[
                    requested_type
                ]

                return (
                    f"file type search {extension}"
                )

        # =================================
        # COMMON WINDOWS FOLDERS
        # =================================

        folders = {

            "desktop": [
                "desktop",
                "my desktop",
                "desktop folder",
                "my desktop folder"
            ],

            "downloads": [
                "download",
                "downloads",
                "my download",
                "my downloads",
                "download folder",
                "downloads folder",
                "my download folder",
                "my downloads folder"
            ],

            "documents": [
                "document",
                "documents",
                "my document",
                "my documents",
                "document folder",
                "documents folder",
                "my document folder",
                "my documents folder"
            ],

            "pictures": [
                "picture",
                "pictures",
                "my picture",
                "my pictures",
                "picture folder",
                "pictures folder",
                "my picture folder",
                "my pictures folder"
            ],

            "videos": [
                "video",
                "videos",
                "my video",
                "my videos",
                "video folder",
                "videos folder",
                "my video folder",
                "my videos folder"
            ],

            "music": [
                "music",
                "my music",
                "music folder",
                "my music folder"
            ]
        }

        # =================================
        # OPEN COMMON FOLDER
        # =================================

        open_folder_patterns = [
            "open",
            "launch",
            "start",
            "show",
            "go to"
        ]

        for action in open_folder_patterns:

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
            r"^(?:create|make|new)\s+"
            r"(?:a\s+)?folder\s+"
            r"(?:called|named)\s+(.+)$",
            text
        )

        if create_match:

            folder_name = (
                create_match.group(1)
                .strip()
            )

            return (
                f"folder create "
                f"{folder_name}"
            )

        # =================================
        # FILE SEARCH
        # =================================

        search_match = re.match(
            r"^(?:find|search for|search)\s+"
            r"(?:my\s+)?(.+)$",
            text
        )

        if search_match:

            query = (
                search_match.group(1)
                .strip()
            )

            if query not in [
                "google",
                "youtube"
            ]:

                return (
                    f"file search "
                    f"{query}"
                )

        # =================================
        # WINDOW CONTROLS
        # =================================

        if text in [
            "minimize this window",
            "minimize the window",
            "minimize window",
            "minimize this",
            "minimize",
        ]:

            return "window minimize"

        if text in [
            "maximize this window",
            "maximize the window",
            "maximize window",
            "maximize this",
            "maximize",
        ]:

            return "window maximize"

        if text in [
            "close this window",
            "close the window",
            "close window",
            "close this",
        ]:

            return "window close"

        if text in [
            "show my desktop",
            "show the desktop",
            "show desktop",
            "go to desktop",
            "go to my desktop",
            "display desktop",
        ]:

            return "window show desktop"

        # =================================
        # CLIPBOARD SEARCH
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

        # =================================
        # CLIPBOARD WRITE
        # =================================

        clipboard_write_match = re.match(
            r"^(?:copy|put|save)\s+(.+?)\s+"
            r"(?:to|into)\s+"
            r"(?:my\s+|the\s+)?clipboard$",
            text
        )

        if clipboard_write_match:

            content = (
                clipboard_write_match.group(1)
                .strip()
            )

            if content:

                return (
                    f"clipboard write "
                    f"{content}"
                )

        # =================================
        # CLIPBOARD CLEAR
        # =================================

        if text in [
            "clear my clipboard",
            "clear the clipboard",
            "empty my clipboard",
            "empty the clipboard",
            "delete my clipboard",
            "delete the clipboard",
        ]:

            return "clipboard clear"

        # =================================
        # CLIPBOARD READ
        # =================================

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
            "tell me what is on my clipboard"
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
        # GOOGLE SEARCH
        # =================================

        google_match = re.match(
            r"^(?:search google for|google search for)\s+(.+)$",
            text
        )

        if google_match:

            query = (
                google_match.group(1)
                .strip()
            )

            return (
                f"google search "
                f"{query}"
            )

        # =================================
        # YOUTUBE SEARCH
        # =================================

        youtube_match = re.match(
            r"^(?:search youtube for|youtube search for)\s+(.+)$",
            text
        )

        if youtube_match:

            query = (
                youtube_match.group(1)
                .strip()
            )

            return (
                f"youtube search "
                f"{query}"
            )

        # =================================
        # OPEN GOOGLE
        # =================================

        if text in [
            "open google",
            "launch google",
            "start google",
        ]:

            return "web open google"

        # =================================
        # OPEN YOUTUBE
        # =================================

        if text in [
            "open youtube",
            "launch youtube",
            "start youtube",
        ]:

            return "web open youtube"

        # =================================
        # OPEN GMAIL
        # =================================

        if text in [
            "open gmail",
            "launch gmail",
            "start gmail",
            "open email",
            "open my email",
        ]:

            return "web open gmail"

        # =================================
        # OPEN GITHUB
        # =================================

        if text in [
            "open github",
            "launch github",
            "start github",
        ]:

            return "web open github"

        # =================================
        # OPEN CHATGPT
        # =================================

        if text in [
            "open chatgpt",
            "open chat gpt",
            "launch chatgpt",
            "launch chat gpt",
            "start chatgpt",
        ]:

            return "web open chatgpt"

        # =================================
        # MEDIA CONTROLS
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
        ]:

            return "media play pause"

        if text in [
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
        # SYSTEM CONTROLS
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
        # MOUSE CONTROLS
        # =================================

        # ---------------------------------
        # MOVE MOUSE TO POSITION
        # ---------------------------------

        if text.startswith("move the mouse to "):

            position = text[
                len("move the mouse to "):
            ].strip()

            position = position.replace(
                "the ",
                "",
                1
            ).strip()

            if position in [
                "centre",
                "center",
                "middle",
                "centre of the screen",
                "center of the screen",
                "middle of the screen"
            ]:

                return "mouse position centre"

        if text.startswith("move mouse to "):

            position = text[
                len("move mouse to "):
            ].strip()

            position = position.replace(
                "the ",
                "",
                1
            ).strip()

            if position in [
                "centre",
                "center",
                "middle",
                "centre of the screen",
                "center of the screen",
                "middle of the screen"
            ]:

                return "mouse position centre"

        # ---------------------------------
        # MOVE MOUSE TO COORDINATES
        # ---------------------------------

        mouse_move_match = re.match(
            r"^move (?:the )?mouse "
            r"(?:to )?(\d+)\s+(\d+)$",
            text
        )

        if mouse_move_match:

            x = mouse_move_match.group(1)
            y = mouse_move_match.group(2)

            return (
                f"mouse move "
                f"{x} {y}"
            )

        # ---------------------------------
        # LEFT CLICK
        # ---------------------------------

        if text in [
            "click",
            "mouse click",
            "left click",
            "left mouse click",
            "click the mouse",
        ]:

            return "mouse click"

        # ---------------------------------
        # DOUBLE CLICK
        # ---------------------------------

        if text in [
            "double click",
            "doubleclick",
            "mouse double click",
            "double click the mouse",
            "double click with the mouse",
        ]:

            return "mouse double click"

        # ---------------------------------
        # RIGHT CLICK
        # ---------------------------------

        if text in [
            "right click",
            "mouse right click",
            "right click the mouse",
            "right click with the mouse",
        ]:

            return "mouse right click"

        # ---------------------------------
        # SCROLL UP
        # ---------------------------------

        if text in [
            "scroll up",
            "scroll upwards",
            "mouse scroll up",
            "scroll up the page",
            "scroll upward",
        ]:

            return "mouse scroll up"

        # ---------------------------------
        # SCROLL DOWN
        # ---------------------------------

        if text in [
            "scroll down",
            "scroll downwards",
            "mouse scroll down",
            "scroll down the page",
            "scroll downward",
        ]:

            return "mouse scroll down"

        # =================================
        # BRIGHTNESS
        # =================================

        if any(
            word in text.split()
            for word in [
                "brightness",
                "bright",
                "dim"
            ]
        ):

            match = re.search(
                r"(?:brightness|bright|screen)\s+"
                r"(?:to\s+)?(\d+)\s*"
                r"(?:percent|%)?",
                text
            )

            if match:

                return (
                    f"brightness set "
                    f"{match.group(1)}"
                )

            if any(
                word in text
                for word in [
                    "increase",
                    "raise",
                    "higher",
                    "up",
                    "brighter"
                ]
            ):

                return "brightness increase"

            if any(
                word in text
                for word in [
                    "decrease",
                    "lower",
                    "down",
                    "dimmer",
                    "dim"
                ]
            ):

                return "brightness decrease"

            return "brightness get"

        # =================================
        # VOLUME
        # =================================

        if any(
            word in text.split()
            for word in [
                "volume",
                "sound",
                "audio",
                "mute",
                "unmute"
            ]
        ):

            if "unmute" in text:

                return "volume unmute"

            if "mute" in text:

                return "volume mute"

            match = re.search(
                r"(?:volume|sound|audio)\s+"
                r"(?:to\s+)?(\d+)\s*"
                r"(?:percent|%)?",
                text
            )

            if match:

                return (
                    f"volume set "
                    f"{match.group(1)}"
                )

            if any(
                word in text
                for word in [
                    "increase",
                    "raise",
                    "higher",
                    "up",
                    "louder"
                ]
            ):

                return "volume increase"

            if any(
                word in text
                for word in [
                    "decrease",
                    "lower",
                    "down",
                    "quieter",
                    "quiet"
                ]
            ):

                return "volume decrease"

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

            city = self.extract_city(
                text
            )

            if city:

                return (
                    f"weather in "
                    f"{city}"
                )

            return "weather"

        # =================================
        # RETURN CLEANED COMMAND
        # =================================

        return text

    # =================================
    # EXTRACT CITY
    # =================================

    def extract_city(self, text):

        patterns = [

            r"\bin\s+([a-zA-Z\s]+)$",

            r"\bat\s+([a-zA-Z\s]+)$",

            r"\bfor\s+([a-zA-Z\s]+)$"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text
            )

            if match:

                city = (
                    match.group(1)
                    .strip()
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