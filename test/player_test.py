import unittest
import sys
sys.path.append('./')
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.name = "Thomas"
        self.uid = "S123"
        self.testPlayer = Player(self.uid, self.name)
        
    def test_uid_datatype(self):
        self.assertIs(self.testPlayer._uid, self.uid)

    def test_name_datatype(self):
        self.assertIs(self.testPlayer._name, self.name)
        
if __name__ in '__main__':
    unittest.main()