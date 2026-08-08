"""
VOICE/listen.py
----------------
Speech recognition engine for NOVA.
"""

import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        # Make NOVA more tolerant of normal background noise
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = 300

        # How long NOVA waits while you are speaking
        self.recognizer.pause_threshold = 0.8

        # Don't stop too quickly after a short pause
        self.recognizer.non_speaking_duration = 0.5

        # Maximum time to wait for speech
        self.recognizer.phrase_threshold = 0.3

        # --------------------------------
        # Microphone
        # --------------------------------

        self.microphone = sr.Microphone()

        print("🎤 Calibrating microphone...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

        print("🎤 Microphone ready.")


    def listen(self):

        with self.microphone as source:

            print("\n🎤 Listening...")

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

                print("🔎 Recognizing...")

                text = self.recognizer.recognize_google(
                    audio
                )

                text = text.lower().strip()

                print(f"You: {text}")

                return text

            except sr.WaitTimeoutError:

                print("❌ No speech detected.")

                return ""

            except sr.UnknownValueError:

                print("❌ Couldn't understand.")

                return ""

            except sr.RequestError as e:

                print(
                    f"❌ Speech Recognition Error: {e}"
                )

                return ""


listener = Listener()