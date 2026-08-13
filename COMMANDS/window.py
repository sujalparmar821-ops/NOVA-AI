"""
COMMANDS/window.py
------------------
Window controls for NOVA.
"""

import ctypes


class Window:

    # =================================
    # GET USER32
    # =================================

    @staticmethod
    def _user32():

        return ctypes.windll.user32

    # =================================
    # GET ACTIVE WINDOW
    # =================================

    def _get_active_window(self):

        user32 = self._user32()

        hwnd = user32.GetForegroundWindow()

        if not hwnd:

            return None

        return hwnd

    # =================================
    # MINIMIZE
    # =================================

    def minimize(self):

        try:

            user32 = self._user32()

            hwnd = self._get_active_window()

            if not hwnd:

                return (
                    "I couldn't find "
                    "an active window."
                )

            SW_MINIMIZE = 6

            user32.ShowWindow(
                hwnd,
                SW_MINIMIZE
            )

            print(
                "NOVA: Window minimized."
            )

            return (
                "Done. I minimized "
                "the window."
            )

        except Exception as e:

            print(
                "Window Minimize Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "minimize the window."
            )

    # =================================
    # MAXIMIZE
    # =================================

    def maximize(self):

        try:

            user32 = self._user32()

            hwnd = self._get_active_window()

            if not hwnd:

                return (
                    "I couldn't find "
                    "an active window."
                )

            SW_MAXIMIZE = 3

            user32.ShowWindow(
                hwnd,
                SW_MAXIMIZE
            )

            print(
                "NOVA: Window maximized."
            )

            return (
                "Done. I maximized "
                "the window."
            )

        except Exception as e:

            print(
                "Window Maximize Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "maximize the window."
            )

    # =================================
    # CLOSE
    # =================================

    def close(self):

        try:

            user32 = self._user32()

            hwnd = self._get_active_window()

            if not hwnd:

                return (
                    "I couldn't find "
                    "an active window."
                )

            WM_CLOSE = 0x0010

            result = user32.PostMessageW(
                hwnd,
                WM_CLOSE,
                0,
                0
            )

            if not result:

                return (
                    "I couldn't close "
                    "the active window."
                )

            print(
                "NOVA: Window close requested."
            )

            return (
                "Done. I closed "
                "the window."
            )

        except Exception as e:

            print(
                "Window Close Error:",
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

            user32 = self._user32()

            VK_LWIN = 0x5B
            VK_D = 0x44

            KEYEVENTF_KEYUP = 0x0002

            # Press Win
            user32.keybd_event(
                VK_LWIN,
                0,
                0,
                0
            )

            # Press D
            user32.keybd_event(
                VK_D,
                0,
                0,
                0
            )

            # Release D
            user32.keybd_event(
                VK_D,
                0,
                KEYEVENTF_KEYUP,
                0
            )

            # Release Win
            user32.keybd_event(
                VK_LWIN,
                0,
                KEYEVENTF_KEYUP,
                0
            )

            print(
                "NOVA: Desktop shown."
            )

            return (
                "Done. I showed "
                "your desktop."
            )

        except Exception as e:

            print(
                "Show Desktop Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "show your desktop."
            )

    # =================================
    # FOCUS APPLICATION
    # =================================

    def focus_app(self, app_name):

        try:

            user32 = self._user32()

            app_name = (
                app_name
                .lower()
                .strip()
            )

            if not app_name:

                return (
                    "Please tell me which "
                    "application to focus."
                )

            matched_window = None

            def enum_windows(hwnd, _):

                nonlocal matched_window

                if not user32.IsWindowVisible(
                    hwnd
                ):

                    return True

                length = (
                    user32.GetWindowTextLengthW(
                        hwnd
                    )
                )

                if length == 0:

                    return True

                buffer = ctypes.create_unicode_buffer(
                    length + 1
                )

                user32.GetWindowTextW(
                    hwnd,
                    buffer,
                    length + 1
                )

                title = buffer.value.lower()

                if app_name in title:

                    matched_window = hwnd

                    return False

                return True

            EnumWindowsProc = ctypes.WINFUNCTYPE(
                ctypes.c_bool,
                ctypes.c_void_p,
                ctypes.c_void_p
            )

            callback = EnumWindowsProc(
                enum_windows
            )

            user32.EnumWindows(
                callback,
                0
            )

            if not matched_window:

                return (
                    f"I couldn't find "
                    f"{app_name}."
                )

            # SW_RESTORE = 9
            user32.ShowWindow(
                matched_window,
                9
            )

            user32.SetForegroundWindow(
                matched_window
            )

            print(
                f"NOVA: Focused {app_name}."
            )

            return (
                f"Done. I switched to "
                f"{app_name}."
            )

        except Exception as e:

            print(
                "Window Focus Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "focus that application."
            )

    # =================================
    # SWITCH NEXT WINDOW
    # =================================

    def switch_next(self):

        try:

            user32 = self._user32()

            VK_MENU = 0x12
            VK_TAB = 0x09

            KEYEVENTF_KEYUP = 0x0002

            # ALT down
            user32.keybd_event(
                VK_MENU,
                0,
                0,
                0
            )

            # TAB down
            user32.keybd_event(
                VK_TAB,
                0,
                0,
                0
            )

            # TAB up
            user32.keybd_event(
                VK_TAB,
                0,
                KEYEVENTF_KEYUP,
                0
            )

            # ALT up
            user32.keybd_event(
                VK_MENU,
                0,
                KEYEVENTF_KEYUP,
                0
            )

            print(
                "NOVA: Switched window."
            )

            return (
                "Done. I switched "
                "to the next window."
            )

        except Exception as e:

            print(
                "Window Switch Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "switch windows."
            )


# =====================================
# CREATE WINDOW MANAGER
# =====================================

window = Window()