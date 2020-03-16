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
            return Human(color, self._ui, self._mic)
        else: # player == 'computer'
            level = self._ui.init_level()
            time  = level + 0.5
            return Computer(color, time)

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
            self._ui.info_board(board)
            while not board.is_game_over():
                self._ui.info_onturn(onturn)
                self._move(board, onturn)
                self._ui.info_board(board)
                onturn = white if onturn == black else black
            self._ui.info_result(board.result())

    # resign() offer_draw()
