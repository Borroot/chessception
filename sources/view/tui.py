import controller.controller
from view.ui import Ui

from model.game.game import ResignException
from model.game.game import DrawOfferException

import re


class Tui(Ui):
    """
    This class provides a terminal user interface.
    """

    def __init__(self, mic, arm, unicode):
        controller.controller.Controller(self, mic, arm, unicode).run()

    def _validate(self, text, regex):
        if re.match(regex, text):
            return True
        else:
            print('Please use the correct answering format.\nFormat: {}'.format(regex))
            return False

    def _ask(self, question, regex):
        print(question)
        response = input('> ')
        if self._validate(response, regex):
            return response
        else:
            return self._ask(question, regex)

    def request_game(self, games):
        question = 'Please choose a game.\n'
        for index, game in enumerate(games):
            question = question + '  ({0}) {1}'.format(index, game)
            question = question + '\n' if index < len(games) - 1 else question
        regex = r'^[0-' + str(len(games) - 1) + r']$'
        answer = games[int(self._ask(question, regex))]
        return answer

    def request_player(self, color):
        question = 'Please choose a player for {}.\n  (0) Human\n  (1) Computer'.format(color)
        regex = r'^[01]$'
        return 'human' if self._ask(question, regex) == '0' else 'computer'

    def request_level(self, levels):
        question = 'Please choose a difficulity level from 1 to {0}.'.format(levels)
        regex = r'^[1-' + str(levels) + r']$'
        return int(self._ask(question, regex))

    def request_move(self, state):
        response = input('> ').lower()
        if response == 'resign':
            raise ResignException()
        elif response == 'draw?':
            raise DrawOfferException()
        else:
            return response

    def request_draw(self):
        question = 'A draw has been offered.\n  (0) Decline\n  (1) Accept.'
        regex = r'^[01]$'
        return True if self._ask(question, regex) == '1' else False

    def show_move_illegal(self, move):
        print('The move {} is invalid.'.format(move))

    def show_state(self, state):
        print()
        print(state)

    def show_speech_talk(self):
        print('Please say your move.')

    def show_speech_error(self):
        print('Your speech could not be recognised.')

    def show_winner(self, winner):
        if winner is None:
            print("It's a draw!")
        else:
            print('The winner is {}!'.format(winner))
