from pyray import measure_text
from raylib import *
from raylib.colors import *
from _game import *
from shared_data import SharedData

class TitlePage():
  "Page to display at start of game"
  def __init__(self):
    self._data = SharedData()
    
  def draw(self):
    "Set page to plain black background with white title"
    BeginDrawing()
    ClearBackground(BLACK)
    text1 = b'Welcome to PONG!'
    lentext1 = measure_text(text1, 100)
    DrawText(text1, int((self._data.MAX_X - lentext1) / 2), int(self._data.MAX_Y / 2), 100, WHITE)
    text2 = b'Press ENTER to begin'
    lentext2 = measure_text(text2, 30)
    DrawText(text2, int((self._data.MAX_X - lentext2) / 2), int(self._data.MAX_Y / 1.4), 30, WHITE)
    text3 = b'Use W/S and UP/DOWN to move the paddles and hit the ball.'
    lentext3 = measure_text(text3, 50)
    DrawText(text3, int((self._data.MAX_X - lentext3) / 2), int(self._data.MAX_Y / 4), 50, WHITE)
    EndDrawing()