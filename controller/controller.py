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
        self._mic = mic
        self._ui  = Tui() if ui == 'tui' else Gui()

        white, black = self._init_players()
        self._game(white, black)

    def _init_players(self):
        white = self._init_player('white')
        black = self._init_player('black')
        return white, black

    def _init_player(self, color):
        player = self._ui.init_player(color)
        if player == 'human':
            return Human(self._ui, self._mic)
        else: # player == 'computer'
            level = self._ui.init_level()
            time  = level + 0.3
            return Computer(time)

    def _move(self, board, player):
        move = player.move(board)
        if move in board.legal_moves:
            board.push(move)
        else:
            self._ui.info_illegal(move)
            self._move(board, player)

    def _game(self, white, black):
        board  = Board()
        onturn = white
        with white, black:
            while not board.is_game_over():
                self._move(board, onturn)
                onturn = white if onturn == black else black
                print(board)
            print(board.result())

    # resign() offer_draw()
