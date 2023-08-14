class Player:
    def __init__(self, _uid: str, _name: str):
        self._uid = _uid
        self._name = _name
        
    def __str__(self):
        return f'Player {self._name} has ID {self._uid}'