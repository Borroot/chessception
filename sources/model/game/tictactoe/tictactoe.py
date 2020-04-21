from model.game.game import Game


class Tictactoe(Game):

    def __init__(self):
        self._board = ['.' for i in range(9)]
        self._moves = []

    def show_state(self):
        builder = ''
        for index, cell in enumerate(self._board):
            builder += str(cell)
            if index == 2 or index == 5:
                builder += '\n'
        return builder

    def state(self):
        return self._board

    def move(self, move):
        if self._board[int(move)] != '.' or int(move) < 0 or int(move) > 8:
            raise ValueError("This move is invalid.")
        if len(self._moves) % 2 == 0:
            self._board[int(move)] = 'X'
        else:
            self._board[int(move)] = 'O'
        self._moves.append(int(move))

    def _won(self):
        """
        Check if the game is won, it does not check if there is a tie!
        :return: The symbol of the winner or None if there is no winner.
        """
        for i in range(3):
            # Check for a horizontal win.
            if self._board[i*3] == self._board[i*3 + 1] == self._board[i*3 + 2] != '.':
                return self._board[i*3]
            # Check for a vertical win.
            if self._board[i] == self._board[i + 3] == self._board[i + 6] != '.':
                return self._board[i]
        # Check for a diagonal win.
        if self._board[0] == self._board[4] == self._board[8] != '.':
            return self._board[0]
        if self._board[2] == self._board[4] == self._board[6] != '.':
            return self._board[2]
        # No one has won, but there might be a tie.
        return None

    def game_over(self):
        # Check if there is a winner.
        if self._won() is not None:
            return True
        # Check if it is a tie.
        for cell in self._board:
            if cell == '.':
                return False
        return True

    def winner(self, white, black):
        assert self.game_over()
        if self._won() == 'X':
            return white
        if self._won() == 'O':
            return black
        return None

    def get_ai(self, color, level):
        pass

    def get_speech(self):
        pass

    def get_dobot(self):
        pass
