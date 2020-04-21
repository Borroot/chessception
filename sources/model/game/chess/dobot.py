import model.hardware.dobot
import chess


class Dobot(model.hardware.dobot.Dobot):

    def __init__(self):
        super().__init__()
        self._white_stack = []  # Contains of white pieces, i.e. pieces taken by black.
        self._black_stack = []  # Contains of black pieces, i.e. pieces taken by white.

    def _convert_uci(self, uci):
        """
        Convert a string representation like 'e4' to a coordinate tuple.
        :return: A coordinate tuple.
        """
        return ord(uci[0]) - ord('a'), int(uci[1]) + 1

    def _next_stack(self, color):
        """
        Calculate the next free position on the given stack.
        :return: A coordinate tuple.
        """
        if color == chess.WHITE:
            return len(self._white_stack) % 8, 11 - int(len(self._white_stack) / 8)
        else:  # color == chess.BLACK
            return len(self._black_stack) % 8, int(len(self._black_stack) / 8)

    def moves(self, game):
        """
        Convert the last move to coordinates which can be understood by the dobot arm.
        """
        # TODO: Add support for promoting.
        move = game.state().pop()  # raises IndexError if empty
        moves = []

        if game.state().is_castling(move):
            turn = game.state().turn
            if game.state().is_kingside_castling(move):
                coordinates_king = ((4, 2), (6, 2)) if turn == chess.WHITE else ((4, 9), (6, 9))
                coordinates_rook = ((7, 2), (5, 2)) if turn == chess.WHITE else ((7, 9), (5, 9))
            else:  # is queenside castling
                coordinates_king = ((4, 2), (2, 2)) if turn == chess.WHITE else ((4, 9), (2, 9))
                coordinates_rook = ((0, 2), (3, 2)) if turn == chess.WHITE else ((0, 9), (3, 9))
            moves.append(coordinates_king)
            moves.append(coordinates_rook)
        else:
            # Free up the square if needed.
            if game.state().is_capture(move):
                index = ord(move.uci()[2]) - ord('a') + (int(move.uci()[3]) - 1) * 8
                piece = game.state().piece_at(chess.SQUARES[index])

                turn = game.state().turn
                if turn == chess.WHITE:
                    coordinates = (self._convert_uci(move.uci()[2:]), self._next_stack(chess.WHITE))
                    moves.append(coordinates)
                    self._black_stack.append(piece)
                else:  # turn == chess.BLACK
                    coordinates = (self._convert_uci(move.uci()[2:]), self._next_stack(chess.BLACK))
                    moves.append(coordinates)
                    self._white_stack.append(piece)

            # Move to the square.
            coordinates = (self._convert_uci(move.uci()[:2]), self._convert_uci(move.uci()[2:4]))
            moves.append(coordinates)

        game.state().push(move)
        return moves

    def move(self, game):
        moves = self.moves(game)
        self.send_all(moves)

        print("White Stack:", self._white_stack)
        print("Black Stack:", self._black_stack)

    def reset(self, game):
        moves_actual = []
        moves_reverse = []

        done = False
        while not done:
            try:
                moves = self.moves(game)
                for move in moves:
                    moves_reverse.append((move[1], move[0]))
                moves_actual.append(game.state().pop())
            except IndexError:
                done = True

        # Restore the final state of the board.
        moves_actual.reverse()
        for move in moves_actual:
            game.state().push(move)

        self._white_stack.clear()
        self._black_stack.clear()
        self.send_all(moves_reverse)
