from model.player.player import Player

class Human(Player):

    def __init__(self, mic):
        super().__init__()
        self.mic = mic
