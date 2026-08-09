"""
COMMANDS/brightness.py
-----------------------
Windows brightness control for NOVA.
"""

import wmi


class BrightnessController:

    def __init__(self):
        self.wmi = wmi.WMI(
            namespace="root\\WMI"
        )

    # --------------------------------
    # Get current brightness
    # --------------------------------

    def get_brightness(self):

        methods = self.wmi.WmiMonitorBrightness()

        if not methods:
            return None

        return methods[0].CurrentBrightness

    # --------------------------------
    # Set brightness
    # --------------------------------

    def set_brightness(self, percentage):

        percentage = max(
            0,
            min(100, int(percentage))
        )

        methods = self.wmi.WmiMonitorBrightnessMethods()

        if not methods:
            return "I couldn't control the screen brightness."

        methods[0].WmiSetBrightness(
            percentage,
            0
        )

        return f"Brightness set to {percentage} percent."

    # --------------------------------
    # Increase brightness
    # --------------------------------

    def increase(self, amount=10):

        current = self.get_brightness()

        if current is None:
            return "I couldn't read the screen brightness."

        new_brightness = min(
            100,
            current + amount
        )

        return self.set_brightness(
            new_brightness
        )

    # --------------------------------
    # Decrease brightness
    # --------------------------------

    def decrease(self, amount=10):

        current = self.get_brightness()

        if current is None:
            return "I couldn't read the screen brightness."

        new_brightness = max(
            0,
            current - amount
        )

        return self.set_brightness(
            new_brightness
        )


brightness = BrightnessController()