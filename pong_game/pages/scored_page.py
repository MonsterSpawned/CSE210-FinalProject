from pyray import measure_text
from raylib import *
from raylib.colors import *
from shared_data import SharedData
from random import *

class ScoredPage:
  "A page which is displayed after a point is scored by either player"

  def __init__(self):
    self._data = SharedData()

  def draw(self, winner, player1, player2):
    BeginDrawing()
    ClearBackground(BLACK)
    text1 = b'Player 1 Score: ' + (str(player1._score).encode())
    DrawText(text1,20,20,60,WHITE)
    text2 = b'Player 2 Score: ' + (str(player2._score).encode())
    lentext2 = measure_text(text2, 60)
    DrawText(text2,self._data.MAX_X - lentext2 - 20,20,60,WHITE)
    text3 = b'Nice Shot ' + str(winner + " !").encode()
    lentext3 = measure_text(text3, 80)
    DrawText(text3, int(self._data.MAX_X / 2) - int(lentext3 / 2), int(self._data.MAX_Y / 2), 80, WHITE)
    text4 = b'Press ENTER to start next round'
    lentext4 = measure_text(text4, 30)
    DrawText(text4, int(self._data.MAX_X / 2) - int(lentext4 / 2), int(self._data.MAX_Y / 1.4), 30, WHITE)
    EndDrawing()