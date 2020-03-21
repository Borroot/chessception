class Ui:
    """
    This abstract class describes a general user interface.
    """

    def __init__(self, controller):
        self._controller = controller
        controller.set_ui(self)

    def show_games(self, games):
        """
        Show the games in the ui.

        :param games: An array with the names of the possible games.
        """

        raise NotImplementedError("Please implement this method.")

    def show_init_player(self, color):
        """
        Show the initialization of a new player.

        :param color: The black or white player.
        :returns: Either 'human' or 'computer'.
        """

        raise NotImplementedError("Please implement this method.")

    def show_init_level(self, levels):
        """
        Show the initialization of the difficulity level for the computer.

        :param levels: The possible difficulity levels.
        :returns: One of the levels.
        """

        raise NotImplementedError("Please implement this method.")

        # r'[a-h][1-8][a-h][1-8][rnbq]?'
