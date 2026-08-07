"""
BRAIN/wake_word.py
------------------
Wake word detection.
"""

from CORE.settings import settings


class WakeWord:
    def __init__(self):
        self.word = settings.get("wake_word", "nova").lower()

    def detected(self, text: str) -> bool:
        if not text:
            return False

        text = text.lower().strip()

        return text == self.word


wake_word = WakeWord()