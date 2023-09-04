class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name
        
    def __repr__(self):
        return f'Player {self._name} has ID {self._uid}'