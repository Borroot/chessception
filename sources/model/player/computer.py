from model.player.player import Player


class Computer(Player):
    """
    This class describes a computer player powered by a chess engine.
    """

    def __init__(self, name, level):
        """
        :param time: Amount of time allowed to think about each move (e.g. 1.0).
        """
        super().__init__(name)
        self._level = level

    def __enter__(self):
        raise NotImplementedError("Please implement this method.")

    def request_move(self, game):
        raise NotImplementedError("Please implement this method.")

    def request_draw(self):
        raise NotImplementedError("Please implement this method.")

    def __exit__(self, exc_type, exc_value, traceback):
        raise NotImplementedError("Please implement this method.")
