import model.player.computer
import random


class Computer(model.player.computer.Computer):

    NUM_LEVELS = 2

    def __init__(self, color, level):
        super().__init__(color, level)

    def __enter__(self):
        return self

    def _move_random(self, game):
        move = random.randint(0, 8)
        while game.board[move] != '.':
            move = random.randint(0, 8)
        return str(move + 1)

    def _heuristic(self, game, symbol):
        if game.won() is None:
            return 0
        else:
            return 1 if game.won() == symbol else -1

    def _negamax(self, game, alpha, beta, color, symbol):
        if game.game_over():
            return color * self._heuristic(game, symbol)

        value = -1000000
        for move in [index for index, cell in enumerate(game.board) if cell == '.']:
            game.board[move] = symbol if color == 1 else ('O' if symbol == 'X' else 'X')
            value = max(value, -self._negamax(game, -beta, -alpha, -color, symbol))
            game.board[move] = '.'

            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    def _move_perfect(self, game):
        symbol = 'X' if len([cell for cell in game.board if cell != '.']) % 2 == 0 else 'O'

        best = -1000000
        bestmoves = []
        for move in [index for index, cell in enumerate(game.board) if cell == '.']:
            game.board[move] = symbol
            value = -self._negamax(game, -1000000, 10000000, -1, symbol)
            game.board[move] = '.'

            if value > best:
                best = value
                bestmoves.clear()
                bestmoves.append(move)
            elif value == best:
                bestmoves.append(move)

        return str(bestmoves[random.randint(0, len(bestmoves) - 1)] + 1)

    def request_move(self, game):
        if self._level == 1:
            return self._move_random(game)
        if self._level == 2:
            return self._move_perfect(game)

    def request_draw(self):
        return False

    def __exit__(self, exc_type, exc_value, traceback):
        pass
