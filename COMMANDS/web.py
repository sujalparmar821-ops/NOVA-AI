"""
COMMANDS/web.py
---------------
Google, YouTube, and website controls for NOVA.
"""

import webbrowser
import urllib.parse


class Web:

    # =================================
    # Google Search
    # =================================

    def google_search(self, query: str):

        query = query.strip()

        if not query:
            return "What should I search for?"

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching Google for {query}."

    # =================================
    # YouTube Search
    # =================================

    def youtube_search(self, query: str):

        query = query.strip()

        if not query:
            return "What should I search for on YouTube?"

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching YouTube for {query}."

    # =================================
    # Open Google
    # =================================

    def open_google(self):

        webbrowser.open(
            "https://www.google.com"
        )

        return "Opening Google."

    # =================================
    # Open YouTube
    # =================================

    def open_youtube(self):

        webbrowser.open(
            "https://www.youtube.com"
        )

        return "Opening YouTube."

    # =================================
    # Open Gmail
    # =================================

    def open_gmail(self):

        webbrowser.open(
            "https://mail.google.com"
        )

        return "Opening Gmail."

    # =================================
    # Open GitHub
    # =================================

    def open_github(self):

        webbrowser.open(
            "https://github.com"
        )

        return "Opening GitHub."

    # =================================
    # Open ChatGPT
    # =================================

    def open_chatgpt(self):

        webbrowser.open(
            "https://chatgpt.com"
        )

        return "Opening ChatGPT."


# =====================================
# Create Web controller
# =====================================

web = Web()


# =====================================
# Compatibility functions
# =====================================
# These keep your existing dispatcher
# imports working.

def google_search(query: str):

    return web.google_search(query)


def youtube_search(query: str):

    return web.youtube_search(query)