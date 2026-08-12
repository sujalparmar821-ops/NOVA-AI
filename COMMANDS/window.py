"""
COMMANDS/window.py
------------------
Window controls for NOVA.
"""

import ctypes


class Window:

    # =================================
    # MINIMIZE ACTIVE WINDOW
    # =================================

    def minimize(self):

        try:

            user32 = ctypes.windll.user32

            hwnd = user32.GetForegroundWindow()

            if not hwnd:

                return "I couldn't find an active window."

            # SW_MINIMIZE = 6
            user32.ShowWindow(
                hwnd,
                6
            )

            print(
                "Window minimized."
            )

            return "Done. I minimized the window."

        except Exception as e:

            print(
                "Window Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "minimize the window."
            )

            # =================================
    # MAXIMIZE ACTIVE WINDOW
    # =================================

    def maximize(self):

        try:

            user32 = ctypes.windll.user32

            hwnd = user32.GetForegroundWindow()

            if not hwnd:

                return "I couldn't find an active window."

            # SW_MAXIMIZE = 3
            user32.ShowWindow(
                hwnd,
                3
            )

            print(
                "Window maximized."
            )

            return "Done. I maximized the window."

        except Exception as e:

            print(
                "Window Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "maximize the window."
            )  

            # =================================
    # CLOSE ACTIVE WINDOW
    # =================================

    def close(self):

        try:

            user32 = ctypes.windll.user32

            hwnd = user32.GetForegroundWindow()

            if not hwnd:

                return "I couldn't find an active window."

            WM_CLOSE = 0x0010

            user32.PostMessageW(
                hwnd,
                WM_CLOSE,
                0,
                0
            )

            print(
                "Window close requested."
            )

            return "Done. I closed the window."

        except Exception as e:

            print(
                "Window Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "close the window."
            )  

            # =================================
    # SHOW DESKTOP
    # =================================

    def show_desktop(self):

        try:

            user32 = ctypes.windll.user32

            # Win + D
            user32.keybd_event(
                0x5B,
                0,
                0,
                0
            )

            user32.keybd_event(
                0x44,
                0,
                0,
                0
            )

            user32.keybd_event(
                0x44,
                0,
                2,
                0
            )

            user32.keybd_event(
                0x5B,
                0,
                2,
                0
            )

            print(
                "Desktop shown."
            )

            return "Done. I showed your desktop."

        except Exception as e:

            print(
                "Window Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "show your desktop."
            )


# =====================================
# CREATE WINDOW MANAGER
# =====================================

window = Window()