"""
COMMANDS/timer.py
-----------------
Timer system for NOVA.
"""

import threading
import time
import winsound

from VOICE.speak import speaker


class Timer:

    def __init__(self):
        self.active_timers = []
        self.cancel_event = threading.Event()

    # =================================
    # START TIMER
    # =================================

    def start(self, seconds: int):

        if seconds <= 0:
            return "The timer needs to be longer than zero."

        # Reset cancellation state
        self.cancel_event.clear()

        timer = threading.Thread(
            target=self._run_timer,
            args=(seconds,),
            daemon=True
        )

        timer.start()

        self.active_timers.append(timer)

        return f"Okay. I've set a timer for {self.format_time(seconds)}."

    # =================================
    # RUN TIMER
    # =================================

    def _run_timer(self, seconds: int):

        # Wait while allowing cancellation
        cancelled = self.cancel_event.wait(seconds)

        if cancelled:
            return

        # 🔔 Timer sound
        winsound.MessageBeep(
            winsound.MB_ICONEXCLAMATION
        )

        # 🎙️ NOVA announcement
        speaker.speak(
            "Hey... your timer is finished."
        )

    # =================================
    # CANCEL TIMER
    # =================================

    def cancel(self):

        self.cancel_event.set()

        return "Okay. I've cancelled your timer."

    # =================================
    # FORMAT TIME
    # =================================

    def format_time(self, seconds: int):

        if seconds < 60:

            return f"{seconds} second{'s' if seconds != 1 else ''}"

        minutes = seconds // 60
        remaining_seconds = seconds % 60

        if remaining_seconds == 0:

            return f"{minutes} minute{'s' if minutes != 1 else ''}"

        return (
            f"{minutes} minute{'s' if minutes != 1 else ''} "
            f"and {remaining_seconds} second"
            f"{'s' if remaining_seconds != 1 else ''}"
        )


timer = Timer()