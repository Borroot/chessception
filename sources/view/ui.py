class Ui:
    """
    This abstract class describes a general user interface.
    """

    def request_game(self, games):
        """
        Request what game to play.
        :param games: A list of games.
        :return: One of the games from the list.
        """

    def request_player(self, name):
        """
        Request a new player.
        :param name: The name of the player.
        :returns: Either 'human' or 'computer'.
        """
        raise NotImplementedError("Please implement this method.")

    def request_level(self, levels):
        """
        Request the difficulity level for the computer player.
        :param levels: The levels ranging from 1 to 'levels'.
        :returns: One of the levels.
        """
        raise NotImplementedError("Please implement this method.")

    def request_move(self, game):
        """
        Request the move which the user wants to make.
        :returns: A move with the following regex r'[a-h][1-8][a-h][1-8][rnbq]?'
        """
        raise NotImplementedError("Please implement this method.")

    def request_draw(self):
        """
        Request the user if he accepts or declines the offer for a draw.
        :returns: True or False.
        """
        raise NotImplementedError("Please implement this method.")

    def show_state(self, state):
        """
        Show the state.
        :param state: A string representation of the state.
        """
        raise NotImplementedError("Please implement this method.")

    def show_move_illegal(self, regex):
        """
        Show information telling that the move is illegal.
        :param regex: The regex for a valid move.
        """
        raise NotImplementedError("Please implement this method.")

    def show_speech_talk(self):
        """
        Show the user has to talk in the microphone.
        """
        raise NotImplementedError("Please implement this method.")

    def show_speech_error(self):
        """
        Show the user that the speech was not recognisable.
        """
        raise NotImplementedError("Please implement this method.")

    def show_winner(self, winner):
        """
        Show the winner of the game.
        :param winner: The winner is None if there is a draw.
        """
        raise NotImplementedError("Please implement this method.")
