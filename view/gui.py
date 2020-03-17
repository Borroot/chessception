from tkinter import *

# TODO Implement all of the functions in this class.
# NOTE Consider switching to PyQt.
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
        print('hi')

    def _screen_start():
        raise NotImplementedError("Please implement this method.")
        # pane = PanedWindow(self.master)
        # pane.pack(fill=BOTH, expand=1)

        # btn_start = Button(self.master, text="START", font=('Arial Bold', 80), command=btn_click_start).pack()
        # pane.add(btn_start)

    def init_player(self, color):
        # raise NotImplementedError("Please implement this method.")
        flag = StringVar(self._master)
        btn_human    = Button(self._master, text='Human'   , command=lambda: flag.set('Human')).pack()
        btn_computer = Button(self._master, text='Computer', command=lambda: flag.set('Computer')).pack()

        pane = PanedWindow(self._master)
        pane.pack(fill=BOTH, expand=1)
        pane.add(btn_human)

        print("waiting...")
        btn_human.wait_variable(var)
        print("done waiting.")
        return 'Human'

    def init_level(self):
        raise NotImplementedError("Please implement this method.")

    def move(self, board):
        # NOTE This could be useful if the mic does not work well.
        raise NotImplementedError("Please implement this method.")

    def info_illegal(self, move):
        raise NotImplementedError("Please implement this method.")
