"""
COMMANDS/mouse.py
-----------------
Mouse controls for NOVA.
"""

import pyautogui


class Mouse:

    # =================================
    # MOVE MOUSE
    # =================================

    def move(self, x, y):

        try:

            pyautogui.moveTo(
                int(x),
                int(y),
                duration=0.2
            )

            return (
                f"Moved the mouse to "
                f"{x}, {y}."
            )

        except Exception as e:

            print(
                "Mouse Move Error:",
                e
            )

            return (
                "Sorry, I couldn't move "
                "the mouse."
            )

    # =================================
    # MOVE TO SCREEN POSITION
    # =================================

    def move_position(self, position):

        try:

            screen_width, screen_height = (
                pyautogui.size()
            )

            position = (
                position
                .lower()
                .strip()
            )

            positions = {

                "centre": (
                    screen_width // 2,
                    screen_height // 2
                ),

                "center": (
                    screen_width // 2,
                    screen_height // 2
                ),

                "middle": (
                    screen_width // 2,
                    screen_height // 2
                ),

                "top left": (
                    10,
                    10
                ),

                "top right": (
                    screen_width - 10,
                    10
                ),

                "bottom left": (
                    10,
                    screen_height - 10
                ),

                "bottom right": (
                    screen_width - 10,
                    screen_height - 10
                ),

                "top centre": (
                    screen_width // 2,
                    10
                ),

                "top center": (
                    screen_width // 2,
                    10
                ),

                "bottom centre": (
                    screen_width // 2,
                    screen_height - 10
                ),

                "bottom center": (
                    screen_width // 2,
                    screen_height - 10
                ),

                "left centre": (
                    10,
                    screen_height // 2
                ),

                "left center": (
                    10,
                    screen_height // 2
                ),

                "right centre": (
                    screen_width - 10,
                    screen_height // 2
                ),

                "right center": (
                    screen_width - 10,
                    screen_height // 2
                ),
            }

            if position not in positions:

                return (
                    f"I don't recognize the "
                    f"mouse position {position}."
                )

            x, y = positions[position]

            pyautogui.moveTo(
                x,
                y,
                duration=0.3
            )

            if position in [
                "centre",
                "center",
                "middle"
            ]:

                return (
                    "Moved the mouse "
                    "to the centre."
                )

            return (
                f"Moved the mouse "
                f"to the {position}."
            )

        except Exception as e:

            print(
                "Mouse Position Error:",
                e
            )

            return (
                "Sorry, I couldn't move "
                "the mouse there."
            )

    # =================================
    # LEFT CLICK
    # =================================

    def click(self):

        try:

            pyautogui.click()

            return "Done. I clicked."

        except Exception as e:

            print(
                "Mouse Click Error:",
                e
            )

            return (
                "Sorry, I couldn't click."
            )

    # =================================
    # DOUBLE CLICK
    # =================================

    def double_click(self):

        try:

            pyautogui.doubleClick()

            return (
                "Done. I double-clicked."
            )

        except Exception as e:

            print(
                "Mouse Double Click Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "double-click."
            )

    # =================================
    # RIGHT CLICK
    # =================================

    def right_click(self):

        try:

            pyautogui.rightClick()

            return (
                "Done. I right-clicked."
            )

        except Exception as e:

            print(
                "Mouse Right Click Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "right-click."
            )

    # =================================
    # SCROLL UP
    # =================================

    def scroll_up(self):

        try:

            pyautogui.scroll(5)

            return (
                "Done. I scrolled up."
            )

        except Exception as e:

            print(
                "Mouse Scroll Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "scroll up."
            )

    # =================================
    # SCROLL DOWN
    # =================================

    def scroll_down(self):

        try:

            pyautogui.scroll(-5)

            return (
                "Done. I scrolled down."
            )

        except Exception as e:

            print(
                "Mouse Scroll Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "scroll down."
            )


# =====================================
# CREATE MOUSE MANAGER
# =====================================

mouse = Mouse()