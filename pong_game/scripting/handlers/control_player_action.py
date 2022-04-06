from shared_data import SharedData

class ControlPlayerAction():
    def __init__(self, keyboard_service):
        self.data = SharedData()
        self.keyboard_service = keyboard_service

def move(self, cast, script):
    if self._keyboard_service.is_key_down('left'):
        self.direction = (0, 0)
    
    if self._keyboard_service.is_key_down('right'):
        self.direction = (-0, 0)
        
    
    