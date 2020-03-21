from model.player.player import Player
import chess.engine

_ENGINE_PATH = "../../stockfish/src/stockfish"


class Computer(Player):
    """
    This abstract class describes a computer player.
    """

    def __init__(self, color):
        super().__init__(color)
        self._level = None

    def set_level(self, level):
        self._level = level

    def __str__(self):
        return self._color + ' (Computer)'

    def __enter__(self):
        raise NotImplementedError("Please implement this method.")

    def move(self, board):
        raise NotImplementedError("Please implement this method.")

    def draw_offer(self):
        raise NotImplementedError("Please implement this method.")

    def __exit__(self, exc_type, exc_value, traceback):
        raise NotImplementedError("Please implement this method.")
