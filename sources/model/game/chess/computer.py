import model.player.computer
import chess.engine


class Computer(model.player.computer.Computer):
    """
    This class describes a computer player powered by a chess engine.
    """

    _ENGINE_PATH = "../../stockfish/src/stockfish"

    def __init__(self, color, time):
        super().__init__(color, time)

    def __enter__(self):
        self._engine = chess.engine.SimpleEngine.popen_uci(self._ENGINE_PATH)
        return self

    def request_move(self, game):
        move = self._engine.play(game.state(), chess.engine.Limit(time=self._time)).move
        return move.__str__()

    def request_draw(self):
        return False

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self._engine.quit()
        except chess.engine.EngineTerminatedError:
            pass
