from model.player.computer_chess import ComputerChess
from model.game.game import Game
import chess
import model.game.chess.board


class Chess(Game):
    LEVELS = 5

    def __init__(self, unicode, invert):
        self._board = model.game.chess.board.Board(unicode, invert)

    def state(self):
        return self._board

    def move(self, move):
        move = chess.Move.from_uci(move)
        if move in self._board.legal_moves:
            self._board.push(move)
        else:
            raise ValueError("The move is invalid.")

    def game_over(self):
        return self._board.is_game_over()

    def winner(self, white, black):
        result = self._board.result()
        if result == '1-0':
            return white
        if result == '0-1':
            return black
        if result == '1/2-1/2':
            return None

    def get_ai(self, color, level):
        return ComputerChess(color, level)
