from model.player.computer_chess import ComputerChess
import model.game.game as game
import chess


class Chess(game.Game):

    LEVELS = 3

    def __init__(self):
        self._board = chess.Board()

    def ai(self, color):
        return ComputerChess(color)

    def state(self):
        return self._board.__str__()

    def move(self, move):
        move = chess.Move.from_uci(move)
        self._board.push(move)

    def valid_move(self, move):
        try:
            move = chess.Move.from_uci(move)
            return move in self._board.legal_moves
        except ValueError:
            return False

    def winner(self, white, black):
        result = self._board.result()
        if result == '1-0':
            return white
        if result == '0-1':
            return black
        if result == '1/2-1/2':
            return None

    def game_over(self):
        return self._board.is_game_over()
