"""
BRAIN/parser.py
---------------
Converts natural language into executable commands.
"""

import re


class Parser:

    def parse(self, text: str) -> str:

        text = text.lower().strip()

        # Remove punctuation
        text = re.sub(r"[^\w\s]", "", text)

        # Common filler words
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

        return " ".join(text.split())


parser = Parser()