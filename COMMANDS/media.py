"""
COMMANDS/media.py
------------------
Windows media controls for NOVA.
"""

import ctypes


class Media:

    # =================================
    # Send Windows media key
    # =================================

    def _press_key(self, key):

        try:

            ctypes.windll.user32.keybd_event(
                key,
                0,
                0,
                0
            )

            ctypes.windll.user32.keybd_event(
                key,
                0,
                2,
                0
            )

            return True

        except Exception as e:

            print(f"MEDIA ERROR: {e}")

            return False

    # =================================
    # Play / Pause
    # =================================

    def play_pause(self):

        if self._press_key(0xB3):

            return "Playing or pausing media."

        return "I couldn't control the media."

    # =================================
    # Next
    # =================================

    def next_track(self):

        if self._press_key(0xB0):

            return "Skipping to the next track."

        return "I couldn't skip the track."

    # =================================
    # Previous
    # =================================

    def previous_track(self):

        if self._press_key(0xB1):

            return "Going to the previous track."

        return "I couldn't go to the previous track."


# =====================================
# Create media controller
# =====================================

media = Media()