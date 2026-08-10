"""
COMMANDS/system.py
------------------
Windows system controls for NOVA.
"""

import subprocess


class System:

    # =================================
    # Lock computer
    # =================================

    def lock(self):

        try:

            subprocess.Popen(
                [
                    "rundll32.exe",
                    "user32.dll,LockWorkStation"
                ]
            )

            return "Locking your computer."

        except Exception as e:

            print(f"SYSTEM ERROR: {e}")

            return "I couldn't lock your computer."

    # =================================
    # Restart computer
    # =================================

    def restart(self):

        try:

            subprocess.Popen(
                [
                    "shutdown",
                    "/r",
                    "/t",
                    "10"
                ]
            )

            return (
                "Your computer will restart "
                "in 10 seconds."
            )

        except Exception as e:

            print(f"SYSTEM ERROR: {e}")

            return "I couldn't restart your computer."

    # =================================
    # Shut down computer
    # =================================

    def shutdown(self):

        try:

            subprocess.Popen(
                [
                    "shutdown",
                    "/s",
                    "/t",
                    "10"
                ]
            )

            return (
                "Your computer will shut down "
                "in 10 seconds."
            )

        except Exception as e:

            print(f"SYSTEM ERROR: {e}")

            return "I couldn't shut down your computer."

    # =================================
    # Cancel shutdown / restart
    # =================================

    def cancel_shutdown(self):

        try:

            subprocess.Popen(
                [
                    "shutdown",
                    "/a"
                ]
            )

            return "The scheduled shutdown was cancelled."

        except Exception as e:

            print(f"SYSTEM ERROR: {e}")

            return "I couldn't cancel the shutdown."


# =====================================
# Create system controller
# =====================================

system = System()