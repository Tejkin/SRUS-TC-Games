from typing import Optional, Sequence
import sys
sys.path.append('./')
from app.player_node import PlayerNode

class PlayerList:
    def __init__(self, values: Sequence = None):
        self._start = None
        
    def is_empty(self):
        if self._start == None:
            return True
        return False
    
    def insert_node(self, playerNode: PlayerNode = None):
        if self._start == None:
            self._start =  playerNode
            return
        return
        