from model.computer.computer import Computer
import chess.engine

_ENGINE_PATH = "../../stockfish/src/stockfish"


class ComputerChess(Computer):
    """
    This class describes a computer player for chess.
    """

    def __init__(self):
        super().__init__()
        self._engine = chess.engine.SimpleEngine.popen_uci(_ENGINE_PATH)

    def move(self, board):
        return self._engine.play(board, chess.engine.Limit(time=self._level)).move

    def close(self):
        self._engine.quit()
