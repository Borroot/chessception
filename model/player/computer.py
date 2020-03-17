from model.player.player import Player
import chess.engine

_ENGINE_PATH = "../stockfish/src/stockfish"

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
        return 'Computer (' + self._color + ')'

    def __enter__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(_ENGINE_PATH)
        return self

    def move(self, board):
        result = self.engine.play(board, chess.engine.Limit(time=self._time))
        return result.move

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.engine.quit()
        except:
            pass
