from model.player.player import Player

class Human(Player):
    """
    This class describes a human player.
    """

    def __init__(self, mic):
        super().__init__()
        self.mic = mic

    def __str__(self):
        return 'Human'
