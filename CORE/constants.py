"""
CORE/constants.py
-----------------
Global constants used throughout NOVA.
"""

# Application
APP_NAME = "NOVA"
APP_VERSION = "1.0.0"

# Voice
WAKE_WORD = "hey nova"

# Logging
LOG_FOLDER = "LOGS"
LOG_FILE = "nova.log"

# Data
DATA_FOLDER = "DATA"
SETTINGS_FILE = "settings.json"
MEMORY_FILE = "memory.json"
HISTORY_FILE = "history.json"

# Supported Commands
SUPPORTED_COMMANDS = [
    "open",
    "search",
    "play",
    "close",
    "shutdown",
    "restart",
]