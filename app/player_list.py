from typing import Optional, Sequence

class PlayerList:
    def __init__(self, values: Sequence = None):
        self._start = None
        
    def is_empty(self):
        if self._start == None:
            return True
        return False