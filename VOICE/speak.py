"""
NOVA Voice Engine
-----------------
Handles all text-to-speech output.
"""

import pyttsx3
from config import VOICE_RATE, VOICE_VOLUME


class Speaker:
    """Text-to-speech engine for NOVA."""

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", VOICE_RATE)
        self.engine.setProperty("volume", VOICE_VOLUME)

    def speak(self, text: str) -> None:
        """Speak the provided text."""

        if not text.strip():
            return

        print(f"NOVA: {text}")

        self.engine.say(text)
        self.engine.runAndWait()


speaker = Speaker()