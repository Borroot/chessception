from model.player.player import Player
import chess.engine


class Computer(Player):
    """
    This class describes a computer player powered by a chess engine.
    """

    _ENGINE_PATH = "../../stockfish/src/stockfish"

    def __init__(self, color, time):
        """
        :param time: Amount of time allowed to think about each move (e.g. 1.0).
        """
        super().__init__(color)
        self._time = time

    def __str__(self):
        return self._color + ' (Computer)'

    def __enter__(self):
        self._engine = chess.engine.SimpleEngine.popen_uci(self._ENGINE_PATH)
        return self

    def request_move(self, board):
        return self._engine.play(board, chess.engine.Limit(time=self._time)).move

    def request_draw(self):
        return False

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self._engine.quit()
        except chess.EngineTerminatedError:
            pass
