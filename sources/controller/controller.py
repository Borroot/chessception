from model.game.chess import Chess
from model.game.checkers import Checkers

from model.game.game import ResignException
from model.game.game import DrawOfferException

from model.player.computer import Computer
from model.player.human import Human

import threading


class Controller(threading.Thread):
    """
    This class controls the flow of the program.
    """

    def __init__(self, ui, mic, arm):
        threading.Thread.__init__(self)
        self._mic = mic
        self._ui = ui

    def run(self):
        game = self._init_game()
        white, black = self._init_players(game)
        winner = self._round(game, white, black)
        self._ui.show_winner(winner)

    def _init_game(self):
        games = ['chess', 'checkers']
        chosen = self._ui.request_game(games)
        return Chess() if chosen == 'chess' else Checkers()

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
            time = level + 0.1
            return Computer(color, time)

    def _move(self, game, player):
        move = player.request_move(game.state())
        try:
            game.move(move)
        except ValueError:
            self._ui.show_move_illegal(move)
            self._move(game, player)

    def _round(self, game, white, black):
        onturn = white
        with white, black:
            self._ui.show_state(game.state())
            while not game.game_over():
                try:
                    self._move(game, onturn)
                    self._ui.show_state(game.state())
                    onturn = game.other(onturn, white, black)
                except ResignException:
                    return game.other(onturn, white, black)
                except DrawOfferException:
                    if game.other(onturn, white, black).request_draw():
                        return None

        return game.winner(white, black)
