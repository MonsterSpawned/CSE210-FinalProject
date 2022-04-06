from actor import Actor

class Ball(Actor):
    """
    Literally a ball.
    
    The ball is to move at the start of the game after countdown and continue moving
    until it hits one side or the other rather than the player's bar.
    
    Attributes: 
        _prepare_body (function) - what the ball looks like
        """
    def __init__(self):
        super().__init__()
        self._prepare_body()

    def _prepare_body(self):
        """
        Creates the body of the ball.

        Returns:
            body shape
        """ 
        body = self._text = "O"
        return body