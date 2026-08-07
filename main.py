"""
NOVA Main Application
Version: 0.1.0
"""

from VOICE.listen import listener
from VOICE.speak import speaker
from BRAIN.wake_word import wake_word
from BRAIN.response import response
from BRAIN.dispatcher import dispatcher


def main():
    speaker.speak("NOVA is now online.")

    while True:
        text = listener.listen()

        if not text:
            continue

        # Exit command
        if text in ["exit", "quit", "goodbye", "stop nova"]:
            speaker.speak("Goodbye.")
            break

        # Wait for wake word
        if not wake_word.detected(text):
            continue

        # Remove wake word from command
        command = text.replace("hey nova", "").strip()

        # User only said "Hey NOVA"
        if command == "":
            speaker.speak(response.greeting())
            continue

        # Execute command
        if dispatcher.dispatch(command):
            continue

        # Unknown command
        speaker.speak(response.unknown_command())


if __name__ == "__main__":
    main()