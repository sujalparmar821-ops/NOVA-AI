"""
COMMANDS/web.py
---------------
Google and YouTube search commands.
"""

import webbrowser
import urllib.parse


def google_search(query: str):
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return True


def youtube_search(query: str):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
    webbrowser.open(url)
    return True