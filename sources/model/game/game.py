class Game:
    """
    This abstract class describes a general game.
    The general game is a two player game with a state and alternating turns.
    """

    def ai_init(self):
        """
        Initialize the ai.
        """
        raise NotImplementedError("Please implement this method.")

    def ai_level(self, level):
        """
        Initialize the difficulity level of the ai.
        """
        raise NotImplementedError("Please implement this method.")

    def ai_move(self):
        """
        Get a move from the ai.

        :returns: Move found by the ai.
        """
        raise NotImplementedError("Please implement this method.")

    def ai_close(self):
        """
        Close the ai, this is useful in case of using an engine.
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

    def winner(self):
        """
        :return: The player which won (either 0 or 1) or None indicating a draw.
        """
        raise NotImplementedError("Please implement this method.")

    def game_over(self):
        """
        :return: If the game has finished.
        """
        raise NotImplementedError("Please implement this method.")
