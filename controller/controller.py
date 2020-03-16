from view.gui import Gui
from view.tui import Tui

class Controller():

    def __init__(self, ui):
        if ui == 'tui':
            self.tui = Tui(self)
        else:
            self.gui = Gui(self)

    # init (initial tests on startup)
    # setplayer() Human() or Computer(level=medium)
    # startgame()
    # forfeit() remise()
