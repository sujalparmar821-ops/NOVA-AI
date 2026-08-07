"""
VOICE/speak.py
--------------
Speech engine for NOVA.
"""

import pyttsx3


class Speaker:

    def speak(self, text: str):
        try:
            print(f"NOVA: {text}")

            # Create a NEW engine every time
            engine = pyttsx3.init()

            engine.setProperty("rate", 180)
            engine.setProperty("volume", 1.0)

            voices = engine.getProperty("voices")
            if len(voices) > 1:
                engine.setProperty("voice", voices[1].id)

            engine.say(text)
            engine.runAndWait()

            engine.stop()

        except Exception as e:
            print("Speech Error:", e)


speaker = Speaker()