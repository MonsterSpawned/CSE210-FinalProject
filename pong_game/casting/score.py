from actor import Actor

class Score(Actor):
    """
    This, as per what you would expect, is where the score is held for each player.
    You will be able to see the score of each respective player on the top two 
    corners of the window.

    The score will go up by one for player 1 when the leftmost wall is hit rather than
    the player itself. Furthermore, player 2's score will raise by one if the 
    rightmost wall is struck rather than colliding with player 2's bar.

    Parameters: 
        _points (int) - The points earned in the game
    """

    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """
        Adds 1 point per each wall hit
        """
        self._points += points
        self.set_text (f"Score: {self._points}")
