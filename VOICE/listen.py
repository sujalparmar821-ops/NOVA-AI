"""
VOICE/listen.py
---------------
Speech recognition engine for NOVA.
"""

import speech_recognition as sr


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5,
                )

                print("🔎 Recognizing...")

                text = self.recognizer.recognize_google(audio)

                print(f"You: {text}")

                return text.lower()

            except sr.WaitTimeoutError:
                print("❌ No speech detected.")
                return ""

            except sr.UnknownValueError:
                print("❌ Couldn't understand.")
                return ""

            except sr.RequestError as e:
                print(f"❌ Speech Recognition Error: {e}")
                return ""


listener = Listener()