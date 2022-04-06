from shared_data import SharedData
from raylib.colors import *

class Actor:
    "Any game element with a position, velocity, color"

    def __init__(self):
        """Constructs a new Actor."""
        self._data = SharedData()
        self._color = WHITE
        self._Xposition = 0
        self._Yposition = 0
        self._Xvelocity = 0
        self._Yvelocity = 0
    
    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return (self._Xposition, self._Yposition)
    
    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return (self._Xvelocity, self._Yvelocity)
    
    def move_actor(self):
        "Move actor according to velocity in both X and Y directions"
        self._Xposition += self._Xvelocity
        self._Yposition += self._Yvelocity
        return self._velocity
    
    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % self._data.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % self._data.MAX_Y
        self._position = (x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, x, y):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._Xposition = x
        self._Yposition = y

    def set_velocity(self, x, y):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._Xvelocity = x
        self._Yvelocity = y
