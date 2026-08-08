"""
COMMANDS/time.py
-----------------
Time and date commands for NOVA.
"""

from datetime import datetime


def get_time():
    now = datetime.now()
    return f"It's {now.strftime('%I:%M %p')}."


def get_date():
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."