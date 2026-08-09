"""
COMMANDS/apps.py
----------------
Fast Windows application finder and launcher for NOVA.
"""

import os
import subprocess
from pathlib import Path


class Apps:

    def __init__(self):

        self.applications = {}

        print("🔎 NOVA is scanning applications...")

        self.scan_applications()

        print(
            f"✅ Found {len(self.applications)} applications."
        )

    # =================================
    # Scan applications
    # =================================

    def scan_applications(self):

        locations = [
            os.path.expandvars(
                r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
            ),

            os.path.expandvars(
                r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs"
            ),

            os.path.expandvars(
                r"%USERPROFILE%\Desktop"
            ),

            os.path.expandvars(
                r"%PUBLIC%\Desktop"
            ),
        ]

        for location in locations:

            path = Path(location)

            if not path.exists():
                continue

            try:

                for file in path.rglob("*"):

                    if file.suffix.lower() in (
                        ".lnk",
                        ".exe",
                        ".url"
                    ):

                        name = file.stem.lower().strip()

                        if name:
                            self.applications[name] = str(file)

            except Exception as e:

                print(
                    f"SCAN ERROR: {e}"
                )

    # =================================
    # Find application
    # =================================

    def find(self, app_name: str):

        app_name = app_name.lower().strip()

        # Exact match
        if app_name in self.applications:

            return self.applications[app_name]

        # Partial match
        for name, path in self.applications.items():

            if app_name in name:

                return path

        return None

    # =================================
    # Open application
    # =================================

    def open(self, app_name: str):

        app_name = app_name.lower().strip()

        path = self.find(app_name)

        # --------------------------------
        # Found application
        # --------------------------------

        if path:

            try:

                # Windows shortcuts
                if path.lower().endswith(
                    (".lnk", ".url")
                ):

                    os.startfile(path)

                # Executables
                else:

                    subprocess.Popen(
                        [path],
                        shell=False
                    )

                return f"Opening {app_name}."

            except Exception as e:

                print(
                    f"APP ERROR: {e}"
                )

        # --------------------------------
        # Windows executable aliases
        # --------------------------------

        try:

            result = subprocess.run(
                [
                    "where",
                    f"{app_name}.exe"
                ],
                capture_output=True,
                text=True,
                shell=True
            )

            if result.returncode == 0:

                lines = result.stdout.strip().splitlines()

                if lines:

                    executable = lines[0].strip()

                    subprocess.Popen(
                        [executable],
                        shell=False
                    )

                    return f"Opening {app_name}."

        except Exception as e:

            print(
                f"ALIAS ERROR: {e}"
            )

        return (
            f"I couldn't find an application "
            f"called {app_name}."
        )

    # =================================
    # Close application
    # =================================

    def close(self, app_name: str):

        app_name = app_name.lower().strip()

        process_aliases = {

            "chrome": "chrome.exe",
            "google chrome": "chrome.exe",

            "spotify": "Spotify.exe",

            "notepad": "notepad.exe",

            "calculator": "CalculatorApp.exe",
            "calc": "CalculatorApp.exe",

            "paint": "mspaint.exe",

            "cmd": "cmd.exe",
            "command prompt": "cmd.exe",

            "powershell": "powershell.exe",

            "file explorer": "explorer.exe",
            "explorer": "explorer.exe",

            "task manager": "Taskmgr.exe",
        }

        process_name = process_aliases.get(
            app_name
        )

        if not process_name:

            process_name = app_name

            if not process_name.endswith(".exe"):

                process_name += ".exe"

        try:

            result = subprocess.run(
                [
                    "taskkill",
                    "/IM",
                    process_name,
                    "/T",
                    "/F"
                ],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:

                return f"Closed {app_name}."

            return (
                f"{app_name} is not currently running."
            )

        except Exception as e:

            print(
                f"CLOSE ERROR: {e}"
            )

            return (
                f"I couldn't close {app_name}."
            )


apps = Apps()