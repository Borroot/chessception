from model.player.computer import Computer
from view.gui import Gui
from view.tui import Tui
from chess    import Board

class Controller():

    def __init__(self, ui, mic):
        if ui == 'tui':
            self.tui = Tui()
        else:
            self.gui = Gui()

        # white = ..
        # black = ..

        # Just some random testing.

        board = Board()
        print(board)
        # print(board.result())
        with Computer(0.1) as ai:
            while not board.is_game_over():
                result = ai.move(board)
                print(result)

                board.push(result.move)
                print(board)

    # Note that 'result' also has
    #   result.draw_offered
    #   result.resigned

    # init (initial tests on startup)
    # setplayer() Human() or Computer(level=medium)
    # startgame()
    # forfeit() remise()
