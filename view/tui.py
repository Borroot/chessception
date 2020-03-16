import signal
import sys
import re

class Tui():
    """
    This class provides a terminal user interface for chessception.
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
                print('Your response does not answer the question correctly.')

    def init_player(self, color):
        question = 'Please choose a player for {}:\n  (0) Human\n  (1) Computer'.format(color)
        regex = r'[01]'
        return 'human' if self._ask(question, regex) == '0' else 'computer'

    def init_level(self):
        question = 'Please choose a difficulity level for the computer.\n  (0) Easy\n  (1) Medium\n  (2) Hard'
        regex = r'[012]'
        return int(self._ask(question, regex))
