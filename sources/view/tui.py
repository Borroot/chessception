from view.ui import Ui
import re


def _ask(question, regex):
    """
    :param question: The question to be displayed to the user.
    :param regex: The regex to validate the answer of the user.
    """

    print(question)
    while True:
        try:
            response = input('> ')
            if re.match(regex, response):
                return response
            else:
                raise ValueError('The response does not answer the question.')
        except ValueError:
            print('Please use the correct answering format.\nFormat: {}'.format(regex))


class Tui(Ui):
    """
    This class provides a terminal user interface.
    """

    def __init__(self, controller, games):
        super().__init__(controller)
        self.show_games(games)

    def show_games(self, games):
        question = 'Please choose a game.\n'
        for index, game in enumerate(games):
            question = question + '  ({0}) {1}'.format(index, game)
            question = question + '\n' if index < len(games) - 1 else question
        regex = r'^[0-' + str(len(games) - 1) + r']$'
        answer = games[int(_ask(question, regex))]
        self._controller.event_game(answer)

    def show_init_player(self, color):
        question = 'Please choose a player for {}.\n  (0) Human\n  (1) Computer'.format(color)
        regex = r'^[01]$'
        answer = 'human' if _ask(question, regex) == '0' else 'computer'
        self._controller.event_init_player(answer, color)

    def show_init_level(self, levels):
        question = 'Please choose a difficulity level.\nThe levels range from 1 to {0}.'.format(levels)
        regex = r'^[1-' + str(levels) + r']$'
        self._controller.event_init_level(int(_ask(question, regex)))

    def show_state(self, state):
        print()
        print(state)

    def show_move(self, state):
        question = 'Please make a move.'
        regex = r'^[a-hA-H][1-8][a-hA-H][1-8][rnbq]?$'
        self._controller.event_move(_ask(question, regex).lower())

    # def show_draw_offer(self):
    #     question = 'A draw has been offered.\n  (0) Decline\n  (1) Accept.'
    #     regex = r'^[01]$'
    #     self._controller.event_draw_offer(True if _ask(question, regex) == '1' else False)
    #
    # def show_winner(self, winner):
    #     if winner is None:
    #         print("It's a draw!")
    #     else:
    #         print('The winner is {}!'.format(winner))
