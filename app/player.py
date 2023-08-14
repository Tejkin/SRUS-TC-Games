class Player():
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        
    def __str__(self):
        return f'Player {self.name} has ID {self.uid}'