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

    def _convert_white_stack(self):
        """
        Calculate the next free position on the white stack.
        :return: A coordinate tuple.
        """
        return len(self._white_stack) % 8, 11 - int(len(self._white_stack) / 8)

    def _convert_black_stack(self):
        """
        Calculate the next free position on the black stack.
        :return: A coordinate tuple.
        """
        return len(self._black_stack) % 8, int(len(self._black_stack) / 8)

    def move(self, game):
        # TODO: Add support for promoting.
        # TODO: Add support for castling.
        moves = []
        move = game.state().pop()

        # Free up the square if needed.
        if game.state().is_capture(move):
            index = ord(move.uci()[2]) - ord('a') + (int(move.uci()[3]) - 1) * 8
            piece = game.state().piece_at(chess.SQUARES[index])

            turn = game.state().turn
            if turn == chess.WHITE:
                coordinates = (self._convert_uci(move.uci()[2:]), self._convert_black_stack())
                moves.append(coordinates)
                self._black_stack.append(piece)
            else:  # turn == chess.BLACK
                coordinates = (self._convert_uci(move.uci()[2:]), self._convert_white_stack())
                moves.append(coordinates)
                self._white_stack.append(piece)

        # Move to the square.
        coordinates = (self._convert_uci(move.uci()[:2]), self._convert_uci(move.uci()[2:4]))
        moves.append(coordinates)

        game.state().push(move)
        self.send_all(moves)

        print("White Stack:", self._white_stack)
        print("Black Stack:", self._black_stack)

    def reset(self, game):
        # TODO: Move all the pieces on the board AND in the stacks to their initial position.
        print("The dobot arm is resetting the board now.")
        pass


