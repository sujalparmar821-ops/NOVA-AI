"""
BRAIN/intent.py
----------------
Determines what kind of thing the user is saying.
"""

from enum import Enum


class Intent(Enum):

    COMMAND = "command"
    QUESTION = "question"
    CONVERSATION = "conversation"


class IntentDetector:

    def detect(self, text: str) -> Intent:

        text = text.lower().strip()

        # =================================
        # COMMANDS
        # =================================

        command_patterns = [

            # Apps
            "open ",
            "launch ",
            "start ",
            "close ",
            "exit ",
            "quit ",

            # Web
            "search ",
            "google ",
            "youtube ",

            # Media
            "play",
            "pause",
            "resume",
            "next",
            "previous",
            "skip",

            # System
            "restart",
            "shutdown",
            "shut down",
            "lock ",
            "cancel ",

            # Volume
            "volume ",
            "sound ",
            "audio ",
            "mute",
            "unmute",

            # Brightness
            "brightness ",
            "bright ",
            "dim ",

            # Screenshot
            "take a screenshot",
            "take screenshot",
            "capture screen",
            "capture my screen",
            "screenshot",

            # Screenshot folder
            "show me my screenshots",
            "show my screenshots",
            "open my screenshots",
            "open screenshots",
            "screenshot folder",

            # Clipboard
            "read my clipboard",
            "read the clipboard",
            "check my clipboard",
            "check the clipboard",
            "what is on my clipboard",
            "whats on my clipboard",
            "tell me whats on my clipboard",
            "tell me what is on my clipboard",
            "show me my clipboard",
            "show my clipboard",

            # Weather
            "weather",
            "temperature",
            "forecast",

            # Time
            "what time is it",
            "what is the time",
            "tell me the time",
            "whats the time",

            # Date
            "what is the date",
            "what is todays date",
            "tell me the date",
            "whats the date",
            "whats todays date",
        ]

        for pattern in command_patterns:

            if text.startswith(pattern):

                return Intent.COMMAND

        # =================================
        # QUESTIONS
        # =================================

        question_words = [
            "what",
            "why",
            "how",
            "when",
            "where",
            "who",
            "which",
            "can you",
            "could you",
            "do you",
            "are you",
            "is it",
        ]

        if text.endswith("?"):

            return Intent.QUESTION

        for word in question_words:

            if text.startswith(word):

                return Intent.QUESTION

        # =================================
        # CONVERSATION
        # =================================

        return Intent.CONVERSATION


intent_detector = IntentDetector()