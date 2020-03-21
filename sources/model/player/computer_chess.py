from model.player.computer import Computer
import chess.engine

_ENGINE_PATH = "../../stockfish/src/stockfish"


class ComputerChess(Computer):
    """
    This class describes a computer player for chess.
    """

    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return super().__str__()

    def __enter__(self):
        self._engine = chess.engine.SimpleEngine.popen_uci(_ENGINE_PATH)
        return self

    def move(self, board):
        result = self._engine.play(board, chess.engine.Limit(time=self._level))
        return result.move

    def draw_offer(self):
        return False

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self._engine.quit()
        except:
            pass
