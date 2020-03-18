class Player():
    """
    This abstract class describes a general player.
    """

    def __init__(self, color):
        self._color = color

    def move(self, board):
        """
        Request the move which the player wants to make.

        :returns: A move with the following regex r'[a-h][1-8][a-h][1-8][rnbq]?'
        """

        raise NotImplementedError("Please Implement this method.")

    def draw_offer(self):
        """
        Request whether the player wants to accept the draw offer.

        :returns: True (accept) or False (decline).
        """

        raise NotImplementedError("Please Implement this method.")
