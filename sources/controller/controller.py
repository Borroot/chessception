from model.player.computer import Computer
from model.player.human import Human

from model.game.chess import Chess

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

        self._players = []
        self._game = None
        self._onturn = None

        games = ['chess', 'checkers']
        self._ui = Tui(self, games) if ui == 'tui' else Gui(self, games)

    def event_game(self, game):
        if game == 'chess':
            self._game = Chess()
        # if game is 'checkers':
        #     self._game = Checkers()
        self._ui.show_init_player('white')

    def event_init_player(self, player, color):
        if player == 'human':
            self._players.append(Human(color))
            if len(self._players) == 1:
                self._ui.show_init_player('black')
            else:
                # TODO: Start the actual game.
                pass

        if player == 'computer':
            self._ui.show_init_level(self._game.levels)

    def event_init_level(self, level):
        self._players.append(Computer(color))

    def _init_player(self, color):
        player = self._ui.init_player(color)
        if player == 'human':
            return Human(color, self._ui, self._mic)
        else:  # player == 'computer'
            level = self._ui.init_level()
            time = level + 0.1
            return Computer(color, time)
