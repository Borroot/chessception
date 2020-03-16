class Ui():
    """
    This class describes a general user interface for chessception.
    """

    def init_player(self, color):
        """
        Initialize a new player.

        :param color: The black or white player.
        :returns: Either 'human' or 'computer'.
        """

        raise NotImplementedError("Please implement this method.")

    def init_level(self):
        """
        Initialize the difficulity level of a computer player.

        :returns: The level 0, 1 or 2.
        """

        raise NotImplementedError("Please implement this method.")
