import unittest
import sys
sys.path.append('./')
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def set_up(self):
        emptyPlayerList = PlayerList()
        filledPlayerList = emptyPlayerList.insert_node()
    def test_    
    