from raylib import *
from shared_data import SharedData

class MovePlayers():
  def __init__(self):
    self._data = SharedData()

  def move_players(self, player1, player2):
    if IsKeyDown(KEY_W) and (player1._Yposition>0):
      player1._Yposition -= self._data.PLAYER_SPEED
      print ("Going Up")
    if IsKeyDown(KEY_S) and (player1._Yposition<self._data.MAX_Y - self._data.PADDLE_WIDTH):
        player1._Yposition += self._data.PLAYER_SPEED
        print ("Going Down")
    if IsKeyDown(KEY_UP) and (player2._Yposition>0):
        player2._Yposition -= self._data.PLAYER_SPEED
        print ("Going Up")
    if IsKeyDown(KEY_DOWN) and (player2._Yposition<self._data.MAX_Y - self._data.PADDLE_WIDTH):
        player2._Yposition += self._data.PLAYER_SPEED
        print ("Going Down")