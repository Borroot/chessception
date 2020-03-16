class Player():
    """
    This abstract class describes a general player.
    """

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

    def move(self, board):
        raise NotImplementedError("Please Implement this method.")
