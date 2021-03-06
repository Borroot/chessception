from model.game.chess.computer import Computer
from model.game.chess.speech import Speech
from model.game.chess.dobot import Dobot
from model.game.game import Game
import chess


class Chess(Game):

    NUM_LEVELS = Computer.NUM_LEVELS
    NUM_PLAYERS = 2

    def __init__(self, unicode, invert):
        self._unicode = unicode
        self._invert = invert
        self._board = chess.Board()

    def show_state(self):
        if self._unicode:
            return self._board.unicode(invert_color=self._invert)
        else:
            return self._board.__str__()

    def state(self):
        return self._board

    def move(self, move):
        try:
            move = chess.Move.from_uci(move)
        except ValueError:
            raise ValueError("The move {} is invalid.\nPlease use valid regex: ^[a-h][1-8][a-h][1-8][rnbq]?$".format(move))

        if move in self._board.legal_moves:
            self._board.push(move)
        else:
            raise ValueError("The move {} is illegal.".format(move))

    def game_over(self):
        return self._board.is_game_over()

    def winner(self, players):
        result = self._board.result()
        if result == '1-0':
            return players[0]
        if result == '0-1':
            return players[1]
        if result == '1/2-1/2':
            return None

    def get_ai(self, color, level):
        return Computer(color, level)

    def get_speech(self):
        return Speech()

    def get_dobot(self):
        return Dobot()

