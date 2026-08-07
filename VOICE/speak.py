"""
VOICE/speak.py
--------------
Speech engine for NOVA.
"""

import pyttsx3


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 180)
        self.engine.setProperty("volume", 1.0)

        voices = self.engine.getProperty("voices")
        if len(voices) > 1:
            self.engine.setProperty("voice", voices[1].id)

    def speak(self, text: str):
        print(f"NOVA: {text}")
        self.engine.say(text)
        self.engine.runAndWait()


speaker = Speaker()