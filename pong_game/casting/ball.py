from pickle import TRUE
from casting.actor import Actor
from shared_data import SharedData
import math

class Ball(Actor):
    """
    This is the player itself, a bar that moves up and down either side of the screen. 

    The goal of the player is to collide with the ball in order to stop the ball from colliding with the wall behind said player.
    """

    def __init__(self):
        super().__init__()
        self._data = SharedData()

    def check_collisions(self, player1, player2):
        #This section of code checks for and handles collisions with the paddle
        if self._Xposition < (self._data.BALL_RADIUS + self._data.PADDLE_THICKNESS):
            if (abs(self._Yposition - (player1._Yposition + (self._data.PADDLE_WIDTH / 2)))) < (self._data.PADDLE_WIDTH / 2):
                print("Hit player1 paddle")
                self._Xvelocity = abs(self._Xvelocity)
        if self._Xposition > (self._data.MAX_X-self._data.PADDLE_THICKNESS - self._data.BALL_RADIUS):
            if (abs(self._Yposition - (player2._Yposition + (self._data.PADDLE_WIDTH / 2)))) < (self._data.PADDLE_WIDTH / 2):
                print("Hit player2 paddle")
                self._Xvelocity = -abs(self._Xvelocity)
        if (self._Yposition < 30 or self._Yposition > self._data.MAX_Y - 30):
            print("bounce")
            self._Yvelocity = abs(self._Yvelocity)
        if (self._Yposition > self._data.MAX_Y - 30):
            self._Yvelocity = - abs(self._Yvelocity)
            print("bounce")

        """if (math.sqrt((self._Xposition ** 2) + ((self._Yposition - player1._Yposition - 50) ** 2))) < 80:
            print("Hit player1 paddle")
            self._Xvelocity = abs(self._Xvelocity)
        if (math.sqrt(((self._Xposition - self._data.MAX_X) ** 2) + ((self._Yposition - player2._Yposition - 50) ** 2))) < 80:
            print("Hit player2 paddle")
            self._Xvelocity = - abs(self._Xvelocity)
        if (self._Yposition < 30 or self._Yposition > self._data.MAX_Y - 30):
            print("bounce")
            self._Yvelocity = abs(self._Yvelocity)
        if (self._Yposition > self._data.MAX_Y - 30):
            self._Yvelocity = - abs(self._Yvelocity)
            print("bounce")
        """
        
    def check_score(self, player1, player2, current_page, last_scored):
        if self._Xposition < 0:
            print ("Player 2 Scored!")
            player2._score += 1
            last_scored = "Player 2"
            current_page = "scored_page"
        if self._Xposition > self._data.MAX_X:
            print ("Player 1 Scored!")
            player1._score += 1
            current_page = "scored_page"
            last_scored = "Player 1"
        return (current_page, last_scored, player1, player2)