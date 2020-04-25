from model.game.game import Game
from model.game.tictactoe.computer import Computer
from model.game.tictactoe.dobot import Dobot
import re


class Tictactoe(Game):

    NUM_LEVELS = Computer.NUM_LEVELS
    NUM_PLAYERS = 2

    def __init__(self):
        self.board = ['.' for i in range(9)]
        self.moves = []

    def show_state(self):
        builder = ''
        for index, cell in enumerate(self.board):
            builder += str(cell)
            if index == 2 or index == 5:
                builder += '\n'
        return builder

    def state(self):
        return self.board

    def move(self, move):
        if not re.match(r'^[1-9]$', move):
            raise ValueError("The move {} is invalid.\nPlease use valid regex: ^[1-9]$".format(move))
        if self.board[int(move) - 1] != '.':
            raise ValueError("The move {} is illegal.\nThe target cell is not empty.".format(move))

        if len(self.moves) % 2 == 0:
            self.board[int(move) - 1] = 'X'
        else:
            self.board[int(move) - 1] = 'O'
        self.moves.append(int(move) - 1)

    def won(self):
        """
        Check if the game is won, it does not check if there is a tie!
        :return: The symbol of the winner or None if there is no winner.
        """
        for i in range(3):
            # Check for a horizontal win.
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] != '.':
                return self.board[i*3]
            # Check for a vertical win.
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != '.':
                return self.board[i]
        # Check for a diagonal win.
        if self.board[0] == self.board[4] == self.board[8] != '.':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != '.':
            return self.board[2]
        # No one has won, but there might be a tie.
        return None

    def game_over(self):
        # Check if there is a winner.
        if self.won() is not None:
            return True
        # Check if it is a tie.
        for cell in self.board:
            if cell == '.':
                return False
        return True

    def winner(self, players):
        if not self.game_over():
            raise ValueError("The game is not game over yet.")
        if self.won() == 'X':
            return players[0]
        if self.won() == 'O':
            return players[1]
        return None

    def get_ai(self, color, level):
        return Computer(color, level)

    def get_speech(self):
        pass

    def get_dobot(self):
        return Dobot()
