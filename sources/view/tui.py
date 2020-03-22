from controller.controller import Controller
from model.exception import ResignException
from model.exception import DrawOfferException
import re

class Tui():
    """
    This class provides a terminal user interface.
    """

    def __init__(self, mic, arm):
        Controller(self, mic, arm).run()

    def _ask(self, question, regex, ismove):
        """
        Ask the user for input.

        :param question: The question to be displayed to the user.
        :param regex: The regex to validate the answer of the user.
        :param ismove: Whether a request for a move is made. This is
        useful since the user is then allowed to resign or offer a draw.

        :raises ResignException:    If 'resign' is typed in and ismove is true.
        :raises DrawOfferException: If 'draw?' is typed in and ismove is true.
        """

        print(question)
        while True:
            try:
                response = input('> ')

                if ismove and re.match(r'^resign$', response, re.I):
                    raise ResignException()
                if ismove and re.match(r'^draw\?$', response, re.I):
                    raise DrawOfferException()

                if re.match(regex, response):
                    return response
                else:
                    raise ValueError('The response does not answer the question.')
            except ValueError:
                print('Please use the correct answering format.\nFormat: {}'.format(regex))

    # def show_games(self, games):
    #     question = 'Please choose a game.\n'
    #     for index, game in enumerate(games):
    #         question = question + '  ({0}) {1}'.format(index, game)
    #         question = question + '\n' if index < len(games) - 1 else question
    #     regex = r'^[0-' + str(len(games) - 1) + r']$'
    #     answer = games[int(_ask(question, regex))]
    #     self._controller.event_game(answer)

    # def show_init_level(self, levels):
    #     question = 'Please choose a difficulity level.\nThe levels range from 1 to {0}.'.format(levels)
    #     regex = r'^[1-' + str(levels) + r']$'
    #     self._controller.event_init_level(int(_ask(question, regex)))

    def init_player(self, color):
        question = 'Please choose a player for {}.\n  (0) Human\n  (1) Computer'.format(color)
        regex = r'^[01]$'
        return 'human' if self._ask(question, regex, False) == '0' else 'computer'

    def init_level(self):
        question = 'Please choose a difficulity level.\n  (0) Easy\n  (1) Medium\n  (2) Hard'
        regex = r'^[012]$'
        return int(self._ask(question, regex, False))

    def move(self, board):
        question = 'Please make a move.'
        regex = r'^[a-hA-H][1-8][a-hA-H][1-8][rnbq]?$'
        return self._ask(question, regex, True).lower()

    def draw_offer(self):
        question = 'A draw has been offered.\n  (0) Decline\n  (1) Accept.'
        regex = r'^[01]$'
        return True if self._ask(question, regex, False) == '1' else False

    def info_illegal(self, move):
        print('The move {} is illegal.'.format(move))

    def info_onturn(self, player):
        pass

    def info_speech(self):
        print('Please say your move.')

    def info_speech_error(self):
        print('Your speech could not be recognised.')

    def info_board(self, board):
        print()
        print(board)

    def info_winner(self, winner):
        if winner == None:
            print("It's a draw!")
        else:
            print('The winner is {}!'.format(winner))
