from typing import Optional

class PlayerNode:
    def __init__(self, player):
        self._player = player
        self.prev_node = Optional[PlayerNode] = None
        self.next_node = Optional[PlayerNode] = None
        
    