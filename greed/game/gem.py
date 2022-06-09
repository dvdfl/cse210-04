from game.moving_object import MovingObject

class Gem(MovingObject):
    """
    Represents the rock (o) objecs
    Inherits from MovingObject

    Attributes:
        _points_value (int): Points when object matches position of player
    """
    def __init__(self):
        """Constructs a new Rock object.
        """
        super().__init__()
        super().set_text("*")
        self._points_value = 1

    def get_points(self):
        """Returns points value of the object.
        
        Returns:
            points (int): Points value of the object if intersected by player.
        """
        return self._points_value
