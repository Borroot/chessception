from model.game.checkers.checkers import Checkers
from model.game.chess.chess import Chess
from model.game.game import ResignException
from model.game.game import DrawOfferException

from model.player.human import Human
import view.tui
import threading


class Controller(threading.Thread):
    """
    This class controls the flow of the program.
    """

    def __init__(self, ui, mic, arm, unicode):
        threading.Thread.__init__(self)
        self._arm = arm
        self._mic = mic
        self._ui = ui
        self._unicode = unicode

    def run(self):
        while True:
            game = self._init_game()
            dobot = game.get_dobot() if self._arm else None
            white, black = self._init_players(game)
            winner = self._round(game, dobot, white, black)
            self._ui.show_winner(winner)
            dobot.reset(game)

    def _init_game(self):
        games = ['chess', 'checkers']
        chosen = self._ui.request_game(games)
        if chosen == 'chess':
            invert = True if type(self._ui) is view.tui.Tui else False
            return Chess(self._unicode, invert)
        elif chosen == 'checkers':
            return Checkers()
        else:
            raise ValueError("A non valid game has been chosen.")

    def _init_players(self, game):
        white = self._init_player(game, 'white')
        black = self._init_player(game, 'black')
        return white, black

    def _init_player(self, game, color):
        player = self._ui.request_player(color)
        if player == 'human':
            return Human(color, self._ui, self._mic)
        else:  # player == 'computer'
            level = self._ui.request_level(game.LEVELS)
            return game.get_ai(color, level)

    def _move(self, game, player):
        move = player.request_move(game)
        try:
            game.move(move)
        except ValueError:
            self._ui.show_move_illegal(move)
            self._move(game, player)

    def _round(self, game, dobot, white, black):
        onturn = white
        with white, black:
            self._ui.show_state(game.show_state())
            while not game.game_over():
                try:
                    self._move(game, onturn)
                    self._ui.show_state(game.show_state())
                    if self._arm:
                        dobot.move(game)
                    onturn = game.other(onturn, white, black)
                except ResignException:
                    return game.other(onturn, white, black)
                except DrawOfferException:
                    if game.other(onturn, white, black).request_draw():
                        return None

        return game.winner(white, black)
