from typing import Optional
from player import Player
class PlayerNode:
    def __init__(self, player: Player = None):
        self._player = player
        self._prev_node = Optional[PlayerNode] = None
        self._next_node = Optional[PlayerNode] = None
        
    def get_player_info(self):
        return self._player
    
    def get_prev_node(self):
        return self._prev_node
    
    def get_next_node(self):
        return self._next_node