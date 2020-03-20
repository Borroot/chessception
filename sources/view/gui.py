import tkinter as tk
import functools


# TODO Implement all of the functions in this class.
# NOTE Switch to PyQt5.
# NOTE Do not forget to implement the exceptions for move.
class Gui(tk.Frame):
    """
    This class provides a graphical user interface.
    """

    def __init__(self, controller, games):
        self._controller = controller
        self._master = tk.Tk()
        tk.Frame.__init__(self, self._master)

        self._master.geometry("800x480")
        self._master.title("Chessception!")

        self.show_games(games)
        self._master.mainloop()

    def show_games(self, games):
        for index, game in enumerate(games):
            event_game = functools.partial(self._controller.event_game, game)
            tk.Button(self._master, text=game, font=('Arial Bold', 40), command=event_game).grid(row=index, column=0)

    def show_init_player(self, color):
        raise NotImplementedError("Please implement this method.")

    def show_init_level(self):
        raise NotImplementedError("Please implement this method.")

    def show_move(self, board):
        # NOTE This could be useful if the mic does not work well.
        raise NotImplementedError("Please implement this method.")

    def info_illegal(self, move):
        raise NotImplementedError("Please implement this method.")
