"""
COMMANDS/volume.py
------------------
Windows volume control for NOVA.
"""

from pycaw.pycaw import AudioUtilities


class VolumeController:

    def __init__(self):

        try:

            devices = AudioUtilities.GetSpeakers()

            self.volume = devices.EndpointVolume

        except Exception as e:

            print(
                "Volume Initialization Error:",
                e
            )

            self.volume = None

    # =================================
    # GET CURRENT VOLUME
    # =================================

    def get_volume(self):

        try:

            if self.volume is None:
                return None

            level = (
                self.volume
                .GetMasterVolumeLevelScalar()
            )

            return round(level * 100)

        except Exception as e:

            print(
                "Volume Read Error:",
                e
            )

            return None

    # =================================
    # SET VOLUME
    # =================================

    def set_volume(self, percentage):

        try:

            percentage = int(
                percentage
            )

            percentage = max(
                0,
                min(100, percentage)
            )

            if self.volume is None:

                return (
                    "I couldn't access "
                    "Windows volume controls."
                )

            self.volume.SetMasterVolumeLevelScalar(
                percentage / 100,
                None
            )

            print(
                f"Volume set to "
                f"{percentage}%."
            )

            return (
                f"Volume set to "
                f"{percentage} percent."
            )

        except Exception as e:

            print(
                "Volume Set Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "change the volume."
            )

    # =================================
    # INCREASE VOLUME
    # =================================

    def increase(self, amount=10):

        try:

            current = self.get_volume()

            if current is None:

                return (
                    "I couldn't read "
                    "the current volume."
                )

            new_volume = min(
                100,
                current + amount
            )

            return self.set_volume(
                new_volume
            )

        except Exception as e:

            print(
                "Volume Increase Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "increase the volume."
            )

    # =================================
    # DECREASE VOLUME
    # =================================

    def decrease(self, amount=10):

        try:

            current = self.get_volume()

            if current is None:

                return (
                    "I couldn't read "
                    "the current volume."
                )

            new_volume = max(
                0,
                current - amount
            )

            return self.set_volume(
                new_volume
            )

        except Exception as e:

            print(
                "Volume Decrease Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "decrease the volume."
            )

    # =================================
    # MUTE
    # =================================

    def mute(self):

        try:

            if self.volume is None:

                return (
                    "I couldn't access "
                    "Windows volume controls."
                )

            self.volume.SetMute(
                1,
                None
            )

            print("Volume muted.")

            return "Volume muted."

        except Exception as e:

            print(
                "Volume Mute Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "mute the volume."
            )

    # =================================
    # UNMUTE
    # =================================

    def unmute(self):

        try:

            if self.volume is None:

                return (
                    "I couldn't access "
                    "Windows volume controls."
                )

            self.volume.SetMute(
                0,
                None
            )

            print("Volume unmuted.")

            return "Volume unmuted."

        except Exception as e:

            print(
                "Volume Unmute Error:",
                e
            )

            return (
                "Sorry, I couldn't "
                "unmute the volume."
            )


# =====================================
# CREATE VOLUME CONTROLLER
# =====================================

volume = VolumeController()