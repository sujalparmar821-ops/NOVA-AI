"""
CORE/settings.py
----------------
Handles loading and saving NOVA settings.
"""

import json
from pathlib import Path


class Settings:

    def __init__(self):
        self.file = Path("DATA/settings.json")

        self.default = {
            "assistant_name": "NOVA",
            "wake_word": "hey nova",
            "voice_rate": 180,
            "voice_volume": 1.0,
            "theme": "dark",
            "debug": False
        }

        self.data = {}
        self.load()

    def load(self):
        if not self.file.exists():
            self.save(self.default)

        with open(self.file, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def save(self, data=None):
        if data is not None:
            self.data = data

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save()


settings = Settings()