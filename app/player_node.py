from typing import Optional
from player import Player
class PlayerNode:
    def __init__(self, player: Player = None):
        self._player = player
        self._prev_node = Optional[PlayerNode] = None
        self._next_node = Optional[PlayerNode] = None
        
    def get_player_info(self):
        return self._player
    
    def get_player_uid(self):
        return self._player._uid
    
    def get_prev_node(self):
        return self._prev_node
    
    def get_next_node(self):
        return self._next_node
    
    def set_player(self, player: Player):
        self._player = player
        
    key = property(fget = get_player_info)
    
    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name} contains player {self._player}'