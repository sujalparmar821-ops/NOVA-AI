"""
COMMANDS/screenshot_folder.py
------------------------------
Opens NOVA's screenshot folder.
"""

import os
import subprocess


class ScreenshotFolder:

    def __init__(self):

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
    # OPEN SCREENSHOT FOLDER
    # =================================

    def open(self):

        try:

            os.startfile(self.folder)

            print(
                f"Screenshots folder opened: {self.folder}"
            )

            return "Sure. I'm opening your screenshots."

        except Exception as e:

            print(
                "Screenshot Folder Error:",
                e
            )

            return (
                "Sorry, I couldn't open "
                "your screenshots folder."
            )


# =====================================
# CREATE MANAGER
# =====================================

screenshot_folder = ScreenshotFolder()