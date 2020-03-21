from model.computer.computer_chess import ComputerChess
import model.game.game as game
import chess


class Chess(game.Game):

    LEVELS = 3

    def __init__(self):
        self._board = chess.Board()
        self._ai = None

    def ai_init(self):
        self._ai = ComputerChess()

    def ai_level(self, level):
        self._ai.set_level(level)

    def ai_move(self):
        return self._ai.move(self._board)

    def ai_close(self):
        if self._ai is not None:
            self._ai.close()

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

    def winner(self):
        result = self._board.result()
        if result == '1-0':
            return 0
        if result == '0-1':
            return 1
        if result == '1/2-1/2':
            return None

    def game_over(self):
        return self._board.is_game_over()
