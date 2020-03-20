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
            if index is not len(games) - 1:
                question = question + '\n'
        regex = r'^[0-' + str(len(games) - 1) + r']$'
        answer = int(_ask(question, regex))
        self._controller.event_game(games[answer])

    def init_player(self, color):
        question = 'Please choose a player for {}.\n  (0) Human\n  (1) Computer'.format(color)
        regex = r'^[01]$'
        return 'human' if _ask(question, regex) == '0' else 'computer'

    def init_level(self):
        question = 'Please choose a difficulity level.\n  (0) Easy\n  (1) Medium\n  (2) Hard'
        regex = r'^[012]$'
        return int(_ask(question, regex))

    def move(self, board):
        question = 'Please make a move.'
        regex = r'^[a-hA-H][1-8][a-hA-H][1-8][rnbq]?$'
        return _ask(question, regex).lower()

    def draw_offer(self):
        question = 'A draw has been offered.\n  (0) Decline\n  (1) Accept.'
        regex = r'^[01]$'
        return True if _ask(question, regex) == '1' else False

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
        if winner is None:
            print("It's a draw!")
        else:
            print('The winner is {}!'.format(winner))
