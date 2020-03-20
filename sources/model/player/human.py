from model.hardware.speech import Speech
from model.player.player   import Player
import chess

class Human(Player):
    """
    This class describes a human player.
    """

    def __init__(self, color, ui, mic):
        super().__init__(color)
        self._ui  = ui
        self._mic = mic

    def __str__(self):
        return self._color + ' (Human)'

    def __enter__(self):
        return self

    def move(self, board):
        if not self._mic:
            return chess.Move.from_uci(self._ui.move(board))
        else:
            speech = Speech()
            try:
                self._ui.info_speech()
                return chess.Move.from_uci(speech.move())
            except:
                self._ui.info_speech_error()
                return move(self, board)

    def draw_offer(self):
        return self._ui.draw_offer()

    def __exit__(self, exc_type, exc_value, traceback):
        pass
