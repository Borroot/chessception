from model.player.player import Player
import chess

class Human(Player):
    """
    This class describes a human player.
    """

    def __init__(self, ui, mic):
        super().__init__()
        self._ui  = ui
        self._mic = mic

    def __str__(self):
        return 'Human'

    def __enter__(self):
        return self

    def move(self, board):
        if not self._mic:
            return chess.Move.from_uci(self._ui.move(board))
        # else:
        #     TODO use the mic

    def __exit__(self, exc_type, exc_value, traceback):
        pass
