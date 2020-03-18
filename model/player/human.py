from model.player.player import Player
import chess
from model.hardware.speech import Speech as vr

class Human(Player):
    """
    This class describes a human player.
    """

    def __init__(self, color, ui, mic):
        super().__init__(color)
        self._ui  = ui
        self._mic = mic

    def __str__(self):
        return 'Human (' + self._color + ')'

    def __enter__(self):
        return self

    def move(self, board):
        if not self._mic:
            return chess.Move.from_uci(self._ui.move(board))
        else:
            voiceRec = vr()
            try:
                print("Say a move:")
                move = chess.Move.from_uci(voiceRec.move())
                return move
            except (ValueError, TypeError):
                print("I did not hear you!")
                return

    def __exit__(self, exc_type, exc_value, traceback):
        pass
