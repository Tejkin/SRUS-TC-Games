import unittest
import sys
sys.path.append('./')
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.emptyPlayerList = PlayerList()
        self.filledPlayerList = self.emptyPlayerList.insert_node()
    def test_is_empty(self):
        self.assertEqual(self.emptyPlayerList.is_empty())
    
if __name__ == '__main__':
    unittest.main()