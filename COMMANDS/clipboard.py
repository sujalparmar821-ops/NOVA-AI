"""
COMMANDS/clipboard.py
----------------------
Clipboard controls for NOVA.
"""

import tkinter as tk


class Clipboard:

    def __init__(self):
        self.root = None

    # =================================
    # GET CLIPBOARD TEXT
    # =================================

    def get_text(self):

        try:

            root = tk.Tk()

            root.withdraw()

            text = root.clipboard_get()

            root.destroy()

            text = text.strip()

            if not text:

                return "Your clipboard is empty."

            # Keep NOVA from reading an extremely
            # large amount of text aloud.

            if len(text) > 500:

                text = text[:500]

                return (
                    f"Your clipboard says: {text}. "
                    "The rest is too long for me to read aloud."
                )

            return f"Your clipboard says: {text}"

        except tk.TclError:

            return "Your clipboard is empty or doesn't contain text."

        except Exception as e:

            print(
                "Clipboard Error:",
                e
            )

            return "Sorry, I couldn't read your clipboard."


            # =================================
    # SET CLIPBOARD TEXT
    # =================================

    def set_text(self, text):

        try:

            text = text.strip()

            if not text:

                return "There is nothing to copy."

            root = tk.Tk()

            root.withdraw()

            root.clipboard_clear()
            root.clipboard_append(text)

            # Keep the clipboard alive after
            # the Tk window is destroyed.
            root.update()

            root.destroy()

            return "Copied to your clipboard."

        except Exception as e:

            print(
                "Clipboard Error:",
                e
            )

            return "Sorry, I couldn't copy that to your clipboard."

        
    # =================================
    # CLEAR CLIPBOARD
    # =================================

    def clear(self):

        try:

            root = tk.Tk()

            root.withdraw()

            root.clipboard_clear()

            root.update()

            root.destroy()

            return "Your clipboard has been cleared."

        except Exception as e:

            print(
                "Clipboard Error:",
                e
            )

            return "Sorry, I couldn't clear your clipboard."

    # =================================
    # GET RAW CLIPBOARD TEXT
    # =================================

    def get_raw_text(self):

        try:

            root = tk.Tk()

            root.withdraw()

            text = root.clipboard_get()

            root.destroy()

            return text.strip()

        except tk.TclError:

            return ""

        except Exception as e:

            print(
                "Clipboard Error:",
                e
            )

            return ""
        
# =====================================
# CREATE CLIPBOARD MANAGER
# =====================================

clipboard = Clipboard()