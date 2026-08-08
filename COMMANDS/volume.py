"""
COMMANDS/volume.py
------------------
Windows volume control for NOVA.
"""

from pycaw.pycaw import AudioUtilities


class VolumeController:

    def __init__(self):

        devices = AudioUtilities.GetSpeakers()

        # Newer pycaw versions expose EndpointVolume directly
        self.volume = devices.EndpointVolume

    # --------------------------------
    # Get current volume
    # --------------------------------

    def get_volume(self):

        level = self.volume.GetMasterVolumeLevelScalar()

        return round(level * 100)

    # --------------------------------
    # Set volume
    # --------------------------------

    def set_volume(self, percentage):

        percentage = max(
            0,
            min(100, int(percentage))
        )

        self.volume.SetMasterVolumeLevelScalar(
            percentage / 100,
            None
        )

        return f"Volume set to {percentage} percent."

    # --------------------------------
    # Increase volume
    # --------------------------------

    def increase(self, amount=10):

        current = self.get_volume()

        new_volume = min(
            100,
            current + amount
        )

        self.volume.SetMasterVolumeLevelScalar(
            new_volume / 100,
            None
        )

        return f"Volume increased to {new_volume} percent."

    # --------------------------------
    # Decrease volume
    # --------------------------------

    def decrease(self, amount=10):

        current = self.get_volume()

        new_volume = max(
            0,
            current - amount
        )

        self.volume.SetMasterVolumeLevelScalar(
            new_volume / 100,
            None
        )

        return f"Volume decreased to {new_volume} percent."

    # --------------------------------
    # Mute
    # --------------------------------

    def mute(self):

        self.volume.SetMute(1, None)

        return "Volume muted."

    # --------------------------------
    # Unmute
    # --------------------------------

    def unmute(self):

        self.volume.SetMute(0, None)

        return "Volume unmuted."


volume = VolumeController()