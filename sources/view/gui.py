import tkinter as tk
import functools


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
        tk.Label(self._master, text=color, font=('Arial Bold', 20)).grid(row=0, column=0)
        for index, player in enumerate(['human', 'computer']):
            event_init_player = functools.partial(self._controller.event_init_player, player)
            tk.Button(self._master, text=player, font=('Arial Bold', 40), command=event_init_player).grid(row=index+1, column=1)

    def show_init_level(self):
        raise NotImplementedError("Please implement this method.")
