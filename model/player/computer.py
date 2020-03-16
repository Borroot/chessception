from model.player.player import Player
import chess.engine

_ENGINE_PATH = "../stockfish/src/stockfish"

# Use the computer class as follows.
# with Computer(0.5) as computer:
    # result = computer.move(board)
    # move = result.move

class Computer(Player):
    """
    This class describes a computer player powered by a chess engine.
    """

    def __init__(self, time):
        """
        :param time: Amount of time allowed to think about each move (e.g. 1.0).
        """
        super().__init__()
        self.time = time

    def __str__(self):
        return 'Computer ({}s)'.format(self.time)

    def __enter__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(_ENGINE_PATH)
        return self

    def move(self, board):
        result = self.engine.play(board, chess.engine.Limit(time=self.time))
        return result.move

    def __exit__(self, exc_type, exc_value, traceback):
        self.engine.quit()
