class Ui():
    """
    This abstract class describes a general user interface for chessception.
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

    def move(self, move):
        """
        Request the move which the user wants to make.

        :returns: A move with the following regex r'[a-h][1-8][a-h][1-8][rnbq]?'
        """

        raise NotImplementedError("Please implement this method.")

    def info_illegal(self, move):
        """
        Show information telling that the move is illegal.
        """

        raise NotImplementedError("Please implement this method.")
