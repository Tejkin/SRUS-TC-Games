import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.testPlayer = Player("S123", "Thomas")
        
    def test_uid_datatype(self):
        self.assertIs(self.testPlayer.uid, str)
        
    def test_name_datatype(self):
        self.assertIs(self.testPlayer.name, str)