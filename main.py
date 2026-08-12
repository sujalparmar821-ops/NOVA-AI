"""
NOVA Main Application
Version: 1.2.1
"""

from VOICE.listen import listener
from VOICE.speak import speaker

from BRAIN.parser import parser
from BRAIN.state import state_manager
from BRAIN.wake_word import wake_word
from BRAIN.dispatcher import dispatcher
from BRAIN.response import response
from BRAIN.conversation import conversation


def main():

    speaker.speak("NOVA is now online.")

    while True:

        # =================================
        # SLEEP TIMEOUT
        # =================================

        if state_manager.timed_out():

            speaker.speak(
                response.sleeping()
            )

            state_manager.sleep()

        # =================================
        # LISTEN
        # =================================

        text = listener.listen()

        if not text:
            continue

        text = text.lower().strip()

        print(
            f"DEBUG HEARD: {text}"
        )

        # =================================
        # EXIT
        # =================================

        if text in [
            "exit",
            "quit",
            "goodbye",
            "stop nova"
        ]:

            speaker.speak(
                response.goodbye()
            )

            break

        # =================================
        # SLEEP MODE
        # =================================

        if not state_manager.is_awake():

            if wake_word.detected(text):

                state_manager.wake()

                speaker.speak(
                    response.greeting()
                )

            continue

        # =================================
        # ACTIVE
        # =================================

        state_manager.update()

        # =================================
        # SLEEP COMMAND
        # =================================

        if text in [
            "go to sleep",
            "sleep",
            "stop listening"
        ]:

            speaker.speak(
                response.sleeping()
            )

            state_manager.sleep()

            continue

        # =================================
        # PARSE FIRST
        # =================================

        command = parser.parse(text)

        print(
            f"DEBUG COMMAND: {command}"
        )

        # =================================
        # TRY COMMAND
        # =================================

        result = dispatcher.dispatch(command)

        print(
            f"DEBUG RESULT: {result}"
        )

        # =================================
        # COMMAND SUCCESS
        # =================================

        if result is not False:

            if isinstance(result, str):

                speaker.speak(result)

            else:

                speaker.speak(
                    response.command_success()
                )

            continue

        # =================================
        # NOT A COMMAND
        # =================================

        result = conversation.respond(text)

        print(
            f"DEBUG CONVERSATION: {result}"
        )

        speaker.speak(result)


# =====================================
# START NOVA
# =====================================

if __name__ == "__main__":

    main()