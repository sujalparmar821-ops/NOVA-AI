"""
COMMANDS/apps.py
----------------
Launch Windows applications.
"""

import subprocess


class Apps:

    APPS = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "command prompt": "cmd.exe",
        "powershell": "powershell.exe",
        "file explorer": "explorer.exe",
    }

    def open(self, app_name: str) -> bool:

        app_name = app_name.lower().strip()

        if app_name not in self.APPS:
            return False

        subprocess.Popen(self.APPS[app_name])

        return True


apps = Apps()