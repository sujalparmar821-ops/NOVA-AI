"""
VOICE/speak.py
--------------
NOVA Neural Speech Engine
"""

import asyncio
import os
import re
import tempfile

import edge_tts
import pygame


class Speaker:

    def __init__(self):

        # =================================
        # VOICE
        # =================================

        self.voice = "en-US-JennyNeural"

        # =================================
        # PYGAME AUDIO
        # =================================

        pygame.mixer.init()

    # =================================
    # CLEAN TEXT
    # =================================

    def clean_text(self, text: str) -> str:

        # Remove emojis and unsupported
        # high Unicode characters
        text = re.sub(
            r"[\U00010000-\U0010ffff]",
            "",
            text
        )

        return text.strip()

    # =================================
    # GENERATE VOICE
    # =================================

    async def _generate(
        self,
        text: str,
        output_file: str
    ):

        communicate = edge_tts.Communicate(
            text,
            self.voice
        )

        await communicate.save(
            output_file
        )

    # =================================
    # SPEAK
    # =================================

    def speak(self, text: str):

        if not text:
            return

        output_file = None

        try:

            # =================================
            # CLEAN TEXT
            # =================================

            text = self.clean_text(text)

            if not text:
                return

            print(f"NOVA: {text}")

            # =================================
            # STOP PREVIOUS SPEECH
            # =================================

            if pygame.mixer.music.get_busy():

                pygame.mixer.music.stop()

            # Unload previously loaded audio
            try:

                pygame.mixer.music.unload()

            except Exception:

                pass

            # =================================
            # CREATE TEMPORARY MP3
            # =================================

            temp_file = tempfile.NamedTemporaryFile(
                prefix="nova_",
                suffix=".mp3",
                delete=False
            )

            output_file = temp_file.name

            temp_file.close()

            # =================================
            # GENERATE SPEECH
            # =================================

            asyncio.run(
                self._generate(
                    text,
                    output_file
                )
            )

            # =================================
            # LOAD AUDIO
            # =================================

            pygame.mixer.music.load(
                output_file
            )

            # =================================
            # PLAY AUDIO
            # =================================

            pygame.mixer.music.play()

            # =================================
            # WAIT UNTIL FINISHED
            # =================================

            clock = pygame.time.Clock()

            while pygame.mixer.music.get_busy():

                clock.tick(20)

            # =================================
            # UNLOAD AUDIO
            # =================================

            try:

                pygame.mixer.music.unload()

            except Exception:

                pass

            # =================================
            # DELETE TEMP FILE
            # =================================

            if os.path.exists(output_file):

                try:

                    os.remove(output_file)

                except Exception:

                    pass

            output_file = None

        except Exception as e:

            print(
                "Speech Error:",
                e
            )

            # =================================
            # CLEAN UP AFTER ERROR
            # =================================

            try:

                pygame.mixer.music.stop()

            except Exception:

                pass

            try:

                pygame.mixer.music.unload()

            except Exception:

                pass

            if output_file and os.path.exists(output_file):

                try:

                    os.remove(output_file)

                except Exception:

                    pass


# =====================================
# Create Speaker
# =====================================

speaker = Speaker()