from model.hardware.speech import Speech
from model.player.player import Player


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

    def request_move(self, state):
        if not self._mic:
            return self._ui.request_move(state)
        else:
            speech = Speech()
            try:
                self._ui.show_speech_talk()
                return speech.move()
            except ValueError:
                self._ui.show_speech_error()
                return self.request_move(state)

    def request_draw(self):
        return self._ui.request_draw()

    def __exit__(self, exc_type, exc_value, traceback):
        pass
