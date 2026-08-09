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

        brightness_words = [
            "brightness",
            "bright",
            "dim",
        ]

        if any(word in text for word in brightness_words):

            # Set brightness

            match = re.search(
                r"(?:brightness|bright|screen)\s+(?:to\s+)?(\d+)\s*(?:percent|%)?",
                text
            )

            if match:

                percentage = match.group(1)

                return f"brightness set {percentage}"

            # Increase brightness

            if any(word in text for word in [
                "increase",
                "raise",
                "higher",
                "up",
                "brighter"
            ]):

                return "brightness increase"

            # Decrease brightness

            if any(word in text for word in [
                "decrease",
                "lower",
                "down",
                "dimmer",
                "dim"
            ]):

                return "brightness decrease"

            # Get brightness

            if "brightness" in text:

                return "brightness get"

        # =================================
        # VOLUME
        # =================================

        volume_words = [
            "volume",
            "sound",
            "audio",
            "mute",
            "unmute",
        ]

        if any(
            word in text.split()
            for word in volume_words
        ):

            # Unmute FIRST
            if "unmute" in text:

                return "volume unmute"

            # Mute

            if "mute" in text:

                return "volume mute"

            # Set volume

            match = re.search(
                r"(?:volume|sound|audio)\s+(?:to\s+)?(\d+)\s*(?:percent|%)?",
                text
            )

            if match:

                percentage = match.group(1)

                return f"volume set {percentage}"

            # Increase volume

            if any(word in text for word in [
                "increase",
                "raise",
                "higher",
                "up",
                "louder"
            ]):

                return "volume increase"

            # Decrease volume

            if any(word in text for word in [
                "decrease",
                "lower",
                "down",
                "quieter",
                "quiet"
            ]):

                return "volume decrease"

            if (
                "volume" in text
                or "sound" in text
            ):

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

        return " ".join(text.split())

    # =================================
    # Extract city from weather command
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