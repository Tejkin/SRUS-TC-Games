import unittest
import sys
sys.path.append('./')
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.emptyPlayerList = PlayerList()
        self.filledPlayerList = PlayerList()
        self.filledPlayerList.insert_node("Test")
        
    def test_is_empty_true(self):
        self.assertEqual(self.emptyPlayerList.is_empty(), True)
        
    def test_is_empty_false(self):
        self.assertEqual(self.filledPlayerList.is_empty(), False)
    
if __name__ == '__main__':
    unittest.main()