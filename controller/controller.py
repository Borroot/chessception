from model.player.computer import Computer
from model.player.human    import Human

from view.gui import Gui
from view.tui import Tui
from chess    import Board

class Controller():
    """
    This class controls the flow of the program and provides an interface
    between the model and the view (conform to the MVC design pattern).
    """

    def __init__(self, ui, mic, arm):
        self.ui = Tui() if ui == 'tui' else Gui()
        self._init_players(mic)

    def _init_players(self, mic):
        self.white = self._init_player(mic, 'white')
        self.black = self._init_player(mic, 'black')

    def _init_player(self, mic, color):
        player = self.ui.init_player(color)
        if player == 'human':
            return Human(self.ui, mic)
        else: # player == 'computer'
            level = self.ui.init_level()
            time  = level + 1.0
            return Computer(time)

    def testing():
        # Just some random testing.
        board = Board()
        print(board)
        # print(board.result())
        with Computer(0.1) as ai:
            while not board.is_game_over():
                result = ai.move(board)
                print(result)

                board.push(result.move)
                print(board)

    # startgame()
    # resign() offer_draw()
