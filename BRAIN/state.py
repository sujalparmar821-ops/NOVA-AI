"""
BRAIN/state.py
"""

from enum import Enum
import time


class BrainState(Enum):
    SLEEPING = 0
    ACTIVE = 1


class StateManager:

    def __init__(self):
        self.state = BrainState.SLEEPING
        self.last_activity = 0

    def wake(self):
        self.state = BrainState.ACTIVE
        self.last_activity = time.time()

    def update(self):
        self.last_activity = time.time()

    def sleep(self):
        self.state = BrainState.SLEEPING

    def is_awake(self):
        return self.state == BrainState.ACTIVE

    def timed_out(self):
        return (
            self.is_awake()
            and time.time() - self.last_activity > 15
        )


state_manager = StateManager()