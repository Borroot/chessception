class Ui():
    """
    This abstract class describes a general user interface.
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

    def info_onturn(self, player):
        """
        Show the player who is on turn.
        """

        raise NotImplementedError("Please implement this method.")

    def info_speech(self):
        """
        Show the user has to talk in the microphone.
        """

        raise NotImplementedError("Please implement this method.")

    def info_speech_error(self):
        """
        Show the user that the speech was not recognisable.
        """

        raise NotImplementedError("Please implement this method.")

    def info_board(self, board):
        """
        Show the board state.
        """

        raise NotImplementedError("Please implement this method.")

    def info_result(self, result):
        """
        Show the result of the game.
        """

        raise NotImplementedError("Please implement this method.")
