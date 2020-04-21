from model.game.tictactoe.tictactoe import Tictactoe
from model.game.chess.chess import Chess
from model.game.game import ResignException
from model.game.game import DrawOfferException

from model.player.human import Human
import view.tui
import threading
from contextlib import ExitStack


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
            players = self._init_players(game)
            winner = self._round(game, dobot, players)
            self._ui.show_winner(winner)
            if self._arm: dobot.reset(game)

    def _init_game(self):
        games = ['chess', 'tic tac toe']
        chosen = self._ui.request_game(games)
        if chosen == 'chess':
            invert = True if type(self._ui) is view.tui.Tui else False
            return Chess(self._unicode, invert)
        elif chosen == 'tic tac toe':
            return Tictactoe()
        else:
            raise ValueError("A non valid game has been chosen.")

    def _init_players(self, game):
        players = []
        for level in range(game.NUM_PLAYERS):
            players.append(self._init_player(game, 'player ' + str(level + 1)))
        return players

    def _init_player(self, game, color):
        player = self._ui.request_player(color)
        if player == 'human':
            return Human(color, self._ui, self._mic)
        else:  # player == 'computer'
            level = self._ui.request_level(game.NUM_LEVELS)
            return game.get_ai(color, level)

    def _move(self, game, player):
        move = player.request_move(game)
        try:
            game.move(move)
        except ValueError as e:
            self._ui.show_move_illegal(str(e))
            self._move(game, player)

    def _round(self, game, dobot, players):
        onturn = 0
        with ExitStack() as stack:
            for player in players:
                stack.enter_context(player)
            self._ui.show_state(game.show_state())
            while not game.game_over():
                try:
                    self._move(game, players[onturn])
                    self._ui.show_state(game.show_state())
                    if self._arm: dobot.move(game)
                    onturn = game.next(onturn, players)
                except ResignException:
                    return players[game.next(onturn, players)]
                except DrawOfferException:
                    if players[game.next(onturn, players)].request_draw():
                        return None
        return game.winner(players)
