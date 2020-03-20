from model.player.computer import Computer
from model.player.human import Human

from view.gui import Gui
from view.tui import Tui


class Controller:
    """
    This class controls the flow of the program and provides an interface
    between the model and the view (conform to the MVC design pattern).
    """

    def __init__(self, ui, mic, arm):
        self._mic = mic
        self._arm = arm

        games = ['Chess', 'Checkers']
        self._ui = Tui(self, games) if ui == 'tui' else Gui(self, games)

        # white, black = self._init_players()
        # winner = self._game(white, black)
        # self._ui.info_winner(winner)

    def event_game(self, game):
        print(game)

    def _init_players(self):
        white = self._init_player('white')
        black = self._init_player('black')
        return white, black

    def _init_player(self, color):
        player = self._ui.init_player(color)
        if player == 'human':
            return Human(color, self._ui, self._mic)
        else:  # player == 'computer'
            level = self._ui.init_level()
            time = level + 0.1
            return Computer(color, time)
