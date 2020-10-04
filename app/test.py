from typing import List


class InvaldEntryException(Exception):
    def __init__(self, entered: str, allowed: List):
        self.entered = entered
        self.allowed = allowed
