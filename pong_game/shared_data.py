from art import tprint
from art.art import DEFAULT_FONT

# Shared variables that can be used for the game without getting a recursive import error.
class SharedData():
    
    # Initialize the shared variables:
    def __init__(self):
        self.CAPTION = "Pong"
        self.MAX_X = 2000
        self.MAX_Y = 1000
        self.FRAME_RATE = 60
        self.CELL_SIZE = 15
        self.FONT_SIZE = 15
        self.PADDLE_WIDTH = 100
        self.PLAYER_SPEED = 15
        self.PADDLE_THICKNESS = 20       
        self.BALL_RADIUS = 30 