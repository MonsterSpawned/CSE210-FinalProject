from casting.actor import Actor

class Player(Actor):
    """
    This is the player itself, a bar that moves up and down either side of the screen. 

    The goal of the player is to collide with the ball in order to stop the ball from colliding with the wall behind said player.
    """

    def __init__(self):
        super().__init__()
        self._score = 0