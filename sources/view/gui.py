from tkinter import *


# TODO Implement all of the functions in this class.
# NOTE Switch to PyQt5.
# NOTE Do not forget to implement the exceptions for move.
class Gui(Frame):
    """
    This class provides a graphical user interface.
    """

    def __init__(self):
        self._master = Tk()
        Frame.__init__(self, self._master)

        self._master.geometry("800x480")
        self._master.title("Chessception!")
        self._master.mainloop()

    def _screen_start(self):
        raise NotImplementedError("Please implement this method.")
        # pane = PanedWindow(self.master)
        # pane.pack(fill=BOTH, expand=1)

        # btn_start = Button(self.master, text="START", font=('Arial Bold', 80), command=btn_click_start).pack()
        # pane.add(btn_start)

    def init_player(self, color):
        raise NotImplementedError("Please implement this method.")

    def init_level(self):
        raise NotImplementedError("Please implement this method.")

    def move(self, board):
        # NOTE This could be useful if the mic does not work well.
        raise NotImplementedError("Please implement this method.")

    def info_illegal(self, move):
        raise NotImplementedError("Please implement this method.")
