class Game:
    """
    This abstract class describes a general game.
    The general game is a two player game with a state and alternating turns.
    """

    def ai(self, color):
        """
        :param color: The color of the player.
        :return: A computer player for this game.
        """
        raise NotImplementedError("Please implement this method.")


    def state(self):
        """
        :return: A string representation of the current state.
        """
        raise NotImplementedError("Please implement this method.")

    def move(self, move):
        """
        Make the move.

        :param move: A string representation of the move to be made.
        """
        raise NotImplementedError("Please implement this method.")

    def valid_move(self, move):
        """
        :param move: A string representation of a move.
        :return: If the move is valid in the current state.
        """
        raise NotImplementedError("Please implement this method.")

    def winner(self, white, black):
        """
        :param white:
        :param black:
        :return: The player which won or None indicating a draw.
        """
        raise NotImplementedError("Please implement this method.")

    def is_game_over(self):
        """
        :return: If the game has finished.
        """
        raise NotImplementedError("Please implement this method.")
