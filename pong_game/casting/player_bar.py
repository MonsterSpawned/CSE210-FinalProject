from actor import Actor

class player_bar(Actor):
    """
    This is the player itself, a bar that moves up and down either side of the screen. 

    The goal of the player is to collide with the ball in order to stop the ball from colliding with the wall behind said player.

    Parameters:
        _prepare_body (str) - creates a the body object of the player, a column of 5 "#" symbols 
    """

    def __init__(self):
        super().__init__()
        self._prepare_body

    def _prepare_body(self):
        """
        Creates the body itself.
        """
        return "#\n#\n#\n#\n#"
