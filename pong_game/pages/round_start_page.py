from raylib import *
from raylib.colors import *
from _game import *
from shared_data import SharedData

class RoundStartPage():
  "Page to display at end of game"
  def __init__(self):
    self._data = SharedData()
    
  def draw(self, player1, player2, ball):
    "Display the players and the ball"
    BeginDrawing()
    ClearBackground(DARKGRAY)
    DrawRectangle(player1._Xposition,player1._Yposition,self._data.PADDLE_THICKNESS,self._data.PADDLE_WIDTH,player1._color)
    DrawRectangle(player2._Xposition,player2._Yposition,self._data.PADDLE_THICKNESS,self._data.PADDLE_WIDTH,player2._color)
    DrawCircle(ball._Xposition, ball._Yposition, self._data.BALL_RADIUS, ball._color)
    EndDrawing()