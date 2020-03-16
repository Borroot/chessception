from model.player.player import Player

class Human(Player):
    """
    This class describes a human player.
    """

    def __init__(self, ui, mic):
        super().__init__()
        self.mic = mic

    def __str__(self):
        return 'Human'

    def move(self, board):
        pass
        # tui, gui or mic
        # validate the move
