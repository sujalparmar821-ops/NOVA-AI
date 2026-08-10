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
        # Remove punctuation
        # =================================

        text = re.sub(r"[^\w\s]", "", text)

        # =================================
        # Common filler words
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
            text = text.replace(word, "")

        text = " ".join(text.split())

        # =================================
        # SYSTEM CONTROLS
        # =================================

        # Cancel shutdown / restart
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

        # Lock computer
        if text in [
            "lock my computer",
            "lock the computer",
            "lock my pc",
            "lock the pc",
            "lock computer",
            "lock pc",
        ]:

            return "system lock"

        # Restart computer
        if text in [
            "restart my computer",
            "restart the computer",
            "restart my pc",
            "restart the pc",
            "restart computer",
            "restart pc",
        ]:

            return "system restart"

        # Shutdown computer
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
        # CLOSE APPLICATION
        # =================================

        close_match = re.match(
            r"^(close|exit|quit|shut down|terminate)\s+(.+)$",
            text
        )

        if close_match:

            app_name = close_match.group(2).strip()

            return f"close {app_name}"

        # =================================
        # OPEN APPLICATION
        # =================================

        app_match = re.match(
            r"^(open|launch|start)\s+(.+)$",
            text
        )

        if app_match:

            app_name = app_match.group(2).strip()

            return f"open {app_name}"

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
                r"(?:brightness|bright|screen)\s+(?:to\s+)?(\d+)\s*(?:percent|%)?",
                text
            )

            if match:

                return f"brightness set {match.group(1)}"

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
                r"(?:volume|sound|audio)\s+(?:to\s+)?(\d+)\s*(?:percent|%)?",
                text
            )

            if match:

                return f"volume set {match.group(1)}"

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

            city = self.extract_city(text)

            if city:

                return f"weather in {city}"

            return "weather"

        # =================================
        # Return cleaned command
        # =================================

        return text

    # =================================
    # Extract city
    # =================================

    def extract_city(self, text: str):

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

                city = match.group(1).strip()

                city = re.sub(
                    r"\b(today|now|tonight|tomorrow)\b",
                    "",
                    city
                ).strip()

                if city:

                    return city

        return None


parser = Parser()