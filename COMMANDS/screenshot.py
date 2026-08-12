"""
COMMANDS/screenshot.py
----------------------
Screenshot system for NOVA.
"""

import os
from datetime import datetime

import pyautogui


class Screenshot:

    def __init__(self):

        # =================================
        # SCREENSHOT FOLDER
        # =================================

        self.folder = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "screenshots"
        )

        os.makedirs(
            self.folder,
            exist_ok=True
        )

    # =================================
    # TAKE SCREENSHOT
    # =================================

    def take(self):

        try:

            # Current date and time
            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            filename = (
                f"screenshot_{timestamp}.png"
            )

            filepath = os.path.join(
                self.folder,
                filename
            )

            # =================================
            # CAPTURE SCREEN
            # =================================

            screenshot = pyautogui.screenshot()

            # =================================
            # SAVE IMAGE
            # =================================

            screenshot.save(filepath)

            print(
                f"Screenshot saved: {filepath}"
            )

            # =================================
            # NOVA RESPONSE
            # =================================

            return "Done. I took a screenshot for you."

        except Exception as e:

            print(
                "Screenshot Error:",
                e
            )

            return (
                "Sorry, I couldn't take "
                "the screenshot."
            )


# =====================================
# CREATE SCREENSHOT MANAGER
# =====================================

screenshot = Screenshot()