class Player:
    """
    This abstract class describes a general player.
    """

    def __init__(self, color):
        self._color = color

    def __str__(self):
        return self._color

    def request_move(self, game):
        """
        Request the move which the player wants to make.
        :returns: A strings representing the move.
        """
        raise NotImplementedError("Please implement this method.")

    def request_draw(self):
        """
        Request whether the player wants to accept the draw offer.
        :returns: True (accept) or False (decline).
        """
        raise NotImplementedError("Please implement this method.")
