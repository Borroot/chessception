from model.player.player import Player


class Computer(Player):
    """
    This class describes a computer player powered by a chess engine.
    """

    def __init__(self, color, time):
        """
        :param time: Amount of time allowed to think about each move (e.g. 1.0).
        """
        super().__init__(color)
        self._time = time

    def __str__(self):
        return self._color + ' (Computer)'

    def __enter__(self):
        raise NotImplementedError("Please implement this method.")

    def request_move(self, board):
        raise NotImplementedError("Please implement this method.")

    def request_draw(self):
        raise NotImplementedError("Please implement this method.")

    def __exit__(self, exc_type, exc_value, traceback):
        raise NotImplementedError("Please implement this method.")
