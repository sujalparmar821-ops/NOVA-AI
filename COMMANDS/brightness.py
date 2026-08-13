"""
COMMANDS/brightness.py
-----------------------
Windows brightness control for NOVA.
"""

import wmi


class BrightnessController:

    def __init__(self):

        try:

            self.wmi = wmi.WMI(
                namespace="root\\WMI"
            )

        except Exception as e:

            print(
                "Brightness WMI Error:",
                e
            )

            self.wmi = None

    # =================================
    # GET CURRENT BRIGHTNESS
    # =================================

    def get_brightness(self):

        try:

            if self.wmi is None:
                return None

            methods = (
                self.wmi.WmiMonitorBrightness()
            )

            if not methods:
                return None

            return int(
                methods[0].CurrentBrightness
            )

        except Exception as e:

            print(
                "Brightness Read Error:",
                e
            )

            return None

    # =================================
    # SET BRIGHTNESS
    # =================================

    def set_brightness(self, percentage):

        try:

            percentage = int(
                percentage
            )

            percentage = max(
                0,
                min(100, percentage)
            )

            if self.wmi is None:

                return (
                    "I couldn't access "
                    "Windows brightness controls."
                )

            methods = (
                self.wmi
                .WmiMonitorBrightnessMethods()
            )

            if not methods:

                return (
                    "Windows didn't provide "
                    "brightness controls for "
                    "this display."
                )

            methods[0].WmiSetBrightness(
                percentage,
                0
            )

            print(
                f"Brightness set to "
                f"{percentage}%."
            )

            return (
                f"Brightness set to "
                f"{percentage} percent."
            )

        except Exception as e:

            print(
                "Brightness Set Error:",
                e
            )

            return (
                "Sorry, I couldn't change "
                "the screen brightness."
            )

    # =================================
    # INCREASE BRIGHTNESS
    # =================================

    def increase(self, amount=10):

        try:

            current = self.get_brightness()

            if current is None:

                return (
                    "I couldn't read the "
                    "current brightness."
                )

            new_brightness = min(
                100,
                current + amount
            )

            return self.set_brightness(
                new_brightness
            )

        except Exception as e:

            print(
                "Brightness Increase Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "increase brightness."
            )

    # =================================
    # DECREASE BRIGHTNESS
    # =================================

    def decrease(self, amount=10):

        try:

            current = self.get_brightness()

            if current is None:

                return (
                    "I couldn't read the "
                    "current brightness."
                )

            new_brightness = max(
                0,
                current - amount
            )

            return self.set_brightness(
                new_brightness
            )

        except Exception as e:

            print(
                "Brightness Decrease Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "decrease brightness."
            )


# =====================================
# CREATE BRIGHTNESS CONTROLLER
# =====================================

brightness = BrightnessController()