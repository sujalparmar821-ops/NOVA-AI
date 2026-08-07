"""
BRAIN/wake_word.py
------------------
Wake word detection for NOVA.
"""

from CORE.settings import settings


class WakeWord:
    def __init__(self):
        self.word = settings.get("wake_word", "hey nova").lower()

    def detected(self, text: str) -> bool:
        if not text:
            return False

        return self.word in text.lower()


wake_word = WakeWord()