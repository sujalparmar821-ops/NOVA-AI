"""
COMMANDS/keyboard.py
--------------------
Keyboard controls for NOVA.
"""

import pyautogui


class Keyboard:

    # =================================
    # PRESS SINGLE KEY
    # =================================

    def press(self, key):

        try:

            pyautogui.press(
                key
            )

            return (
                f"Done. I pressed "
                f"{key}."
            )

        except Exception as e:

            print(
                "Keyboard Press Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                f"press {key}."
            )

    # =================================
    # PRESS KEY COMBINATION
    # =================================

    def hotkey(self, *keys):

        try:

            pyautogui.hotkey(
                *keys
            )

            combination = " + ".join(
                keys
            )

            return (
                f"Done. I pressed "
                f"{combination}."
            )

        except Exception as e:

            print(
                "Keyboard Hotkey Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "press that key combination."
            )

    # =================================
    # TYPE TEXT
    # =================================

    def type_text(self, text):

        try:

            pyautogui.write(
                text,
                interval=0.02
            )

            return "Done. I typed it."

        except Exception as e:

            print(
                "Keyboard Type Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "type that."
            )


# =====================================
# CREATE KEYBOARD MANAGER
# =====================================

keyboard = Keyboard()