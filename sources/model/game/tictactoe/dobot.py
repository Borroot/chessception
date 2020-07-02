import model.hardware.dobot


class Dobot(model.hardware.dobot.Dobot):
    """
    This class describes coordinate conversions and a board reset function for tic tac toe which can be used
    for the dobot arm. The physical board layout is as follows.

        +---+---+---+
      6 |   |   |   | = self._o_stack
        +---+---+---+
      5 |   |   |   | O's PIECES
        +---+---+---+

        +---+---+---+
      4 |   |   |   |
        +---+---+---+
      3 |   |   |   |
        +---+---+---+
      2 |   |   |   |
        +---+---+---+

        +---+---+---+
      1 |   |   |   | X's PIECES
        +---+---+---+
      0 |   |   |   | = self._x_stack
        +---+---+---+
          0   1   2
    """

    def __init__(self):
        super().__init__(1)
        self._x_stack = 5  # Contains the X's pieces.
        self._o_stack = 5  # Contains the O's pieces.

    def _convert_move(self, move):
        """
        Convert an int representation like 0, 1, .., 8 to a coordinate tuple.
        :return: A coordinate tuple.
        """
        return move % 3, 2 + int((8 - move) / 3)

    def _update_stack(self, symbol, diff):
        if symbol == 'X':
            self._x_stack += diff
        else:  # symbol == 'O'
            self._o_stack += diff

    def _next_stack(self, symbol):
        """
        Calculate the next piece position on the given stack.
        :return: A coordinate tuple.
        """
        if symbol == 'X':
            coordinate = (self._x_stack % 3, int(self._x_stack / 3))
            return coordinate
        else:  # symbol == 'O'
            coordinate = (self._o_stack % 3, 6 - int(self._o_stack / 3))
            return coordinate

    def _moves(self, game):
        symbol = 'O' if len([cell for cell in game.board if cell != '.']) % 2 == 0 else 'X'
        move = game.moves.pop()
        moves = [(self._next_stack(symbol), self._convert_move(move))]
        self._update_stack(symbol, -1)
        game.moves.append(move)
        return moves

    def move(self, game):
        moves = self._moves(game)
        self.send_all(moves)

    def reset(self, game):
        moves = []
        self._serial_port.write("<GAME OVER>".encode('ascii'))
        for move, symbol in enumerate(game.board):
            self._update_stack(symbol, 1)
            moves.append((self._convert_move(move), self._next_stack(symbol)))
        self._x_stack = 5
        self._o_stack = 5
        self.send_all(moves)
