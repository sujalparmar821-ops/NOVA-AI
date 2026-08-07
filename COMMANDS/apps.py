"""
COMMANDS/apps.py
"""

import subprocess

from VOICE.speak import speaker

APPS = {
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
}


def open_app(command: str):

    command = command.lower()

    for app_name, executable in APPS.items():

        if app_name in command:

            speaker.speak(f"Opening {app_name}")

            subprocess.Popen(executable)

            return True

    return False