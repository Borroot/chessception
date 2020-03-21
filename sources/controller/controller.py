from model.player.human import Human
from model.game.chess import Chess

from view.gui import Gui
from view.tui import Tui


class Controller:
    """
    This class controls the flow of the program.
    """

    def __init__(self, ui, mic, arm):
        self._mic = mic
        self._arm = arm
        self._ui = None

        self._players = []
        self._game = None
        self._onturn = None  # index of the player on turn

        games = ['chess', 'checkers']
        Tui(self, games) if ui == 'tui' else Gui(self, games)

    def set_ui(self, ui):
        self._ui = ui

    def event_move(self, move):
        if self._game.valid_move(move):
            self._game.move(move)
            self._ui.show_state(self._game.state())

        if self._game.game_over():
            winner = self._game.winner(self._players[0], self._players[1])
            # show winner
        else:
            self._onturn = (self._onturn + 1) % len(self._players)
            if isinstance(self._players[self._onturn], Human):
                self._ui.show_move()
            else:
                self.event_move(self._players)

    def event_game(self, game):
        if game == 'chess':
            self._game = Chess()
        # if game is 'checkers':
        #     self._game = Checkers()
        self._init_players()

    def _init_players(self):
        if len(self._players) < 2:
            colors = ['white', 'black']
            self._ui.show_init_player(colors[len(self._players)])
        else:  # the players are initialized
            self._onturn = 0
            self.event_move("")

    def event_init_player(self, player, color):
        if player == 'human':
            self._players.append(Human(color))
            self._init_players()
        if player == 'computer':
            self._players.append(self._game.ai(color))
            self._ui.show_init_level(self._game.LEVELS)

    def event_init_level(self, level):
        self._players[len(self._players) - 1].set_level(level)
        self._init_players()
