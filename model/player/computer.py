from model.player.player import Player
import chess.engine

ENGINE_PATH = "../stockfish/src/stockfish"

# Use the computer class as follows.
# with Computer() as computer:
    # result = computer.move(board)
    # move = result.move

class Computer(Player):

    def __init__(self, time):
        super().__init__()
        self.time = time

    def __enter__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(ENGINE_PATH)
        return self

    def move(self, board):
        return self.engine.play(board, chess.engine.Limit(time=self.time))

    def __exit__(self, exc_type, exc_value, traceback):
        self.engine.quit()
