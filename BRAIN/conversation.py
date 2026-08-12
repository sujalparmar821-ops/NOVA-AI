"""
BRAIN/conversation.py
---------------------
NOVA's natural conversation and personality engine.
"""

import random
import re


class Conversation:

    def __init__(self):

        self.history = []
        self.last_emotion = "neutral"

    # =================================
    # MAIN RESPONSE ENGINE
    # =================================

    def respond(self, text: str) -> str:

        text = text.lower().strip()

        if not text:
            return "Hmm?"

        # Remember conversation
        self.history.append(text)

        if len(self.history) > 30:
            self.history.pop(0)

        emotion = self.detect_emotion(text)
        self.last_emotion = emotion

        # ---------------------------------
        # GREETINGS
        # ---------------------------------

        if self.matches(text, [
            "hi",
            "hello",
            "hey",
            "hey nova",
            "hello nova",
        ]):

            return random.choice([
                "Heyy.",
                "Hey, what's up?",
                "Heyy, I'm listening.",
                "Yo 😭 what's going on?",
                "Hey. How are you doing?",
            ])

        # ---------------------------------
        # HOW ARE YOU
        # ---------------------------------

        if self.matches(text, [
            "how are you",
            "how are you doing",
            "how are you feeling",
        ]):

            return random.choice([
                "I'm good. What's going on with you?",
                "I'm alright. You sound like you've got something on your mind though.",
                "Pretty good. But enough about me, how are you?",
            ])

        # ---------------------------------
        # THANK YOU
        # ---------------------------------

        if self.matches(text, [
            "thanks",
            "thank you",
            "thankyou",
        ]):

            return random.choice([
                "Anytime.",
                "Of course.",
                "You got it.",
                "No worries.",
                "Always.",
            ])

        # ---------------------------------
        # TIRED
        # ---------------------------------

        if emotion == "tired":

            return random.choice([
                "Yeahh... you sound exhausted. Take a little break.",
                "I can kinda hear it in your voice. You've been going for a while, haven't you?",
                "Damn, you're tired tired 😭. Maybe give yourself a few minutes.",
                "You don't have to force yourself through everything. Take a breather.",
            ])

        # ---------------------------------
        # SAD
        # ---------------------------------

        if emotion == "sad":

            return random.choice([
                "Yeah... something feels off. What happened?",
                "You don't sound okay. Wanna talk about it?",
                "Hmm... you seem a little down. I'm listening.",
                "Okay... tell me what's going on.",
            ])

        # ---------------------------------
        # ANGRY
        # ---------------------------------

        if emotion == "angry":

            return random.choice([
                "Okayyy... somebody's pissed 😭. What happened?",
                "Yeah, I can tell you're annoyed. What did they do?",
                "Damn. What happened?",
                "Alright, talk to me. What's got you this angry?",
            ])

        # ---------------------------------
        # STRESSED
        # ---------------------------------

        if emotion == "stressed":

            return random.choice([
                "Yeah... sounds like you've got way too much going on.",
                "One thing at a time. What's stressing you out the most?",
                "Take a breath for a second. We can figure it out.",
                "Okay, slow down. Tell me what's going on.",
            ])

        # ---------------------------------
        # HAPPY / EXCITED
        # ---------------------------------

        if emotion == "happy":

            return random.choice([
                "Okayyy, I can hear the excitement 😂. What happened?",
                "Wait, you're actually happy about something. Tell me.",
                "I like this energy 😭. What happened?",
                "Alright, somebody's having a good day.",
            ])

        # ---------------------------------
        # BORED
        # ---------------------------------

        if self.contains(text, [
            "i am bored",
            "im bored",
            "i'm bored",
            "so bored",
            "bored today",
        ]):

            return random.choice([
                "Bored already? 😭 We need to fix that.",
                "Hmm... okay, let's find something interesting.",
                "You're bored and somehow decided to bother me. 😂",
                "Alright, what are we doing then?",
            ])

        # ---------------------------------
        # CAN'T SLEEP
        # ---------------------------------

        if self.contains(text, [
            "cant sleep",
            "can't sleep",
            "cannot sleep",
            "i cant sleep",
            "i can't sleep",
        ]):

            return random.choice([
                "Still awake? Your brain really said 'nope' tonight 😭.",
                "Can't sleep? Wanna talk for a bit?",
                "Yeah... sometimes your brain just refuses to shut up.",
                "What are you thinking about?",
            ])

        # ---------------------------------
        # COMPLIMENT
        # ---------------------------------

        if self.contains(text, [
            "you are good",
            "you're good",
            "you are amazing",
            "you're amazing",
            "you are smart",
            "you're smart",
            "good job",
            "nice job",
        ]):

            return random.choice([
                "Hehe, I'll take that.",
                "Okayyy, don't make my ego too big 😂.",
                "Thanks. I'm getting there.",
                "See? I'm useful sometimes. 😌",
            ])

        # ---------------------------------
        # USER SAYS NOVA IS BAD
        # ---------------------------------

        if self.contains(text, [
            "you're annoying",
            "you are annoying",
            "you're useless",
            "you are useless",
            "you're bad",
            "you are bad",
        ]):

            return random.choice([
                "Damn 😭 okay, what did I do?",
                "Alright alright, tell me what I messed up.",
                "Fair enough. What should I have done?",
                "Okay, I'll take the criticism 😂.",
            ])

        # ---------------------------------
        # GOODBYE
        # ---------------------------------

        if self.matches(text, [
            "bye",
            "goodbye",
            "good night",
            "goodnight",
            "see you",
            "see you later",
        ]):

            return random.choice([
                "Alright, see you later.",
                "Okayy, take care.",
                "Goodnight. Get some rest.",
                "See you soon.",
            ])

        # ---------------------------------
        # FOLLOW-UP
        # ---------------------------------

        if text in [
            "yeah",
            "yes",
            "yep",
            "okay",
            "ok",
            "sure",
        ]:

            return self.follow_up_response()

        if text in [
            "no",
            "nope",
            "nah",
            "not really",
        ]:

            return random.choice([
                "Alright, fair enough.",
                "Okay, I get you.",
                "Yeah, that's fine.",
                "Gotcha.",
            ])

        # ---------------------------------
        # QUESTION
        # ---------------------------------

        if text.endswith("?"):

            return random.choice([
                "Hmm... let me think.",
                "Good question.",
                "I get what you're asking.",
                "Yeah, that's interesting.",
            ])

        # ---------------------------------
        # GENERIC HUMAN RESPONSE
        # ---------------------------------

        return random.choice([
            "Hmm... tell me more.",
            "Yeah? Go on.",
            "I'm listening.",
            "Okay, I'm with you.",
            "I get you.",
            "What happened?",
            "And then?",
            "Hmm... interesting.",
            "Yeah, I know what you mean.",
        ])

    # =================================
    # EMOTION
    # =================================

    def detect_emotion(self, text: str) -> str:

        if self.contains(text, [
            "tired",
            "exhausted",
            "sleepy",
            "drained",
            "no energy",
        ]):

            return "tired"

        if self.contains(text, [
            "sad",
            "upset",
            "lonely",
            "crying",
            "hurt",
            "heartbroken",
            "feeling down",
        ]):

            return "sad"

        if self.contains(text, [
            "angry",
            "mad",
            "pissed",
            "furious",
            "annoyed",
            "irritated",
        ]):

            return "angry"

        if self.contains(text, [
            "stressed",
            "overwhelmed",
            "too much",
            "pressure",
        ]):

            return "stressed"

        if self.contains(text, [
            "happy",
            "excited",
            "amazing",
            "awesome",
            "great",
            "finally",
            "won",
        ]):

            return "happy"

        return "neutral"

    # =================================
    # FOLLOW-UP RESPONSE
    # =================================

    def follow_up_response(self):

        if self.last_emotion == "tired":

            return random.choice([
                "Yeah... then definitely take that break.",
                "Good. Don't push yourself too hard.",
            ])

        if self.last_emotion == "sad":

            return random.choice([
                "Yeah... I'm listening.",
                "Okay. Tell me what happened.",
            ])

        if self.last_emotion == "angry":

            return random.choice([
                "Yeah. What happened?",
                "Okay, talk to me.",
            ])

        if self.last_emotion == "happy":

            return random.choice([
                "Haha, I knew it 😂.",
                "I can tell you're happy about it.",
            ])

        return random.choice([
            "Alright.",
            "Yeah, I'm with you.",
            "Okay, go on.",
            "Got you.",
        ])

    # =================================
    # MATCH
    # =================================

    @staticmethod
    def matches(text: str, phrases: list) -> bool:

        return text in phrases

    # =================================
    # CONTAINS
    # =================================

    @staticmethod
    def contains(text: str, phrases: list) -> bool:

        return any(
            phrase in text
            for phrase in phrases
        )


# =====================================
# NOVA CONVERSATION INSTANCE
# =====================================

conversation = Conversation()