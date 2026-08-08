"""
NOVA Main Application
Version: 1.0.0
"""

from VOICE.listen import listener
from VOICE.speak import speaker

from BRAIN.parser import parser
from BRAIN.state import state_manager
from BRAIN.wake_word import wake_word
from BRAIN.dispatcher import dispatcher
from BRAIN.response import response


def main():

    speaker.speak("NOVA is now online.")

    while True:

        # Go back to sleep after inactivity
        if state_manager.timed_out():
            speaker.speak(response.sleeping())
            state_manager.sleep()

        text = listener.listen()

        if not text:
            continue

        # Exit NOVA completely
        if text.lower() in [
            "exit",
            "quit",
            "goodbye",
            "stop nova"
        ]:
            speaker.speak(response.goodbye())
            break

        # -----------------------------
        # SLEEP MODE
        # -----------------------------
        if not state_manager.is_awake():

            if wake_word.detected(text):
                state_manager.wake()
                speaker.speak(response.greeting())

            continue

        # -----------------------------
        # ACTIVE MODE
        # -----------------------------
        state_manager.update()

        # User wants NOVA to sleep
        if text.lower() in [
            "go to sleep",
            "sleep",
            "stop listening"
        ]:
            speaker.speak(response.sleeping())
            state_manager.sleep()
            continue

        # -----------------------------
        # PARSE COMMAND
        # -----------------------------
        command = parser.parse(text)

        # -----------------------------
        # EXECUTE COMMAND
        # -----------------------------
        result = dispatcher.dispatch(command)
        print(f"DEBUG RESULT: {result}")

        if isinstance(result, str):
            speaker.speak(result)

        elif result:
            speaker.speak(response.command_success())

        else:
            speaker.speak(response.unknown_command())


if __name__ == "__main__":
    main()