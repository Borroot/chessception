class Player():
    """
    This abstract class describes a general player.
    """

    def __init__(self, color):
        self._color = color

    def move(self, board):
        raise NotImplementedError("Please Implement this method.")
