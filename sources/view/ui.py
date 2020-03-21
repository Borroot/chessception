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
        """

        raise NotImplementedError("Please implement this method.")

    def show_init_level(self, levels):
        """
        Show the initialization of the difficulity level for the computer.

        :param levels: The possible difficulity levels.
        """

        raise NotImplementedError("Please implement this method.")

    def show_state(self, state):
        """
        Show the state in the ui.

        :param state: A string representation of the state.
        """

        raise NotImplementedError("Please implement this method.")

    def show_move(self, state):
        """
        Show the request for a move in the ui.
        """

        raise NotImplementedError("Please implement this method.")
