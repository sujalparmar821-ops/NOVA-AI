"""
BRAIN/response.py
-----------------
NOVA voice responses.
"""

import random


class Response:

    def greeting(self):
        return random.choice([
            "Yes?",
            "I'm listening.",
            "Go ahead.",
            "How can I help?"
        ])

    def command_success(self):
        return random.choice([
            "Done.",
            "Right away.",
            "On it.",
            "Okay."
        ])

    def sleeping(self):
        return "Going back to sleep."

    def unknown_command(self):
        return random.choice([
            "I don't know how to do that yet.",
            "I'm still learning that command.",
            "Sorry, I can't do that yet."
        ])

    def goodbye(self):
        return "Goodbye."


response = Response()