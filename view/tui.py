import signal
import sys
import re

class Tui():
    """
    This class provides a terminal user interface.
    """

    def _ask(self, question, regex):
        """
        Ask the user for input.

        :param question: The question to be displayed to the user.
        :param regex: The regex to validate the answer of the user.
        """

        print(question)
        while True:
            try:
                response = input('> ')
                match = re.match(regex, response)
                if match:
                    return response
                else:
                    raise ValueError('The response does not answer the question.')
            except ValueError:
                print('Please use the correct answering format.\nFormat: {}'.format(regex))

    def init_player(self, color):
        question = 'Please choose a player for {}:\n  (0) Human\n  (1) Computer'.format(color)
        regex = r'[01]'
        return 'human' if self._ask(question, regex) == '0' else 'computer'

    def init_level(self):
        question = 'Please choose a difficulity level for the computer.\n  (0) Easy\n  (1) Medium\n  (2) Hard'
        regex = r'[012]'
        return int(self._ask(question, regex))

    def move(self, board):
        question = 'Please make a move.'
        regex = r'[a-hA-H][1-8][a-hA-H][1-8][rnbq]?'
        return self._ask(question, regex).lower()

    def info_illegal(self, move):
        print('The move {} is illegal.'.format(move))

    def info_onturn(self, player):
        # print('{} is on turn.'.format(player))
        pass

    def info_board(self, board):
        print()
        print(board)

    def info_result(self, result):
        print('The final result is {}!'.format(result))
