import re


def _ask(question, regex):
    """
    Ask the user for input.

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


class Tui:
    """
    This class provides a terminal user interface.
    """

    def __init__(self, controller, games):
        self._controller = controller
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
        self._controller.event_init_player(answer)

    def show_init_level(self, levels):
        question = 'Please choose a difficulity level.\n  (0) Easy\n  (1) Medium\n  (2) Hard'
        regex = r'^[012]$'
        return int(_ask(question, regex))

    ########################################################################################################

    def show_state(self, state):
        print()
        print(state)

    def show_move(self, board):
        question = 'Please make a move.'
        regex = r'^[a-hA-H][1-8][a-hA-H][1-8][rnbq]?$'
        return _ask(question, regex).lower()

    def show_move_error(self, move):
        print('The move {} is illegal.'.format(move))

    def show_speech(self):
        print('Please say your move.')

    def show_speech_error(self):
        print('Your speech could not be recognised.')

    def show_draw_offer(self):
        question = 'A draw has been offered.\n  (0) Decline\n  (1) Accept.'
        regex = r'^[01]$'
        return True if _ask(question, regex) == '1' else False

    def show_onturn(self, player):
        pass

    def show_winner(self, winner):
        if winner is None:
            print("It's a draw!")
        else:
            print('The winner is {}!'.format(winner))
