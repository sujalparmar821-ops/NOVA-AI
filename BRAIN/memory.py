"""
BRAIN/memory.py
---------------
Persistent memory system for NOVA.
"""

import json
import os


class Memory:

    def __init__(self):

        self.file = os.path.join(
            os.path.dirname(__file__),
            "memory.json"
        )

        self.data = {}

        self.load()

    # =================================
    # LOAD MEMORY
    # =================================

    def load(self):

        try:

            if os.path.exists(self.file):

                with open(
                    self.file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    self.data = json.load(f)

            else:

                self.data = {}

        except Exception as e:

            print(
                "Memory Load Error:",
                e
            )

            self.data = {}

    # =================================
    # SAVE MEMORY
    # =================================

    def save(self):

        try:

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    self.data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

        except Exception as e:

            print(
                "Memory Save Error:",
                e
            )

    # =================================
    # REMEMBER
    # =================================

    def remember(self, key: str, value: str):

        key = key.lower().strip()

        self.data[key] = value.strip()

        self.save()

        return True

    # =================================
    # RECALL
    # =================================

    def recall(self, key: str):

        key = key.lower().strip()

        return self.data.get(key)

    # =================================
    # FORGET
    # =================================

    def forget(self, key: str):

        key = key.lower().strip()

        if key in self.data:

            del self.data[key]

            self.save()

            return True

        return False

    # =================================
    # GET EVERYTHING
    # =================================

    def all_memories(self):

        return self.data.copy()

    # =================================
    # CLEAR EVERYTHING
    # =================================

    def clear(self):

        self.data = {}

        self.save()

        return True


# =====================================
# NOVA MEMORY INSTANCE
# =====================================

memory = Memory()