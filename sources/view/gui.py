from view.ui import Ui
import tkinter as tk
import functools


class Gui(Ui, tk.Frame):
    """
    This class provides a graphical user interface.
    """

    def __init__(self, controller, games):
        super().__init__(controller)
        self._master = tk.Tk()
        tk.Frame.__init__(self, self._master)

        self._master.geometry("800x480")
        self._master.title("Chessception!")

        self.show_games(games)
        self._master.mainloop()

    def _clear(self):
        for widget in self._master.winfo_children():
            widget.destroy()

    def show_games(self, games):
        self._clear()
        for index, game in enumerate(games):
            padding = (100, 10) if index == 0 else 10
            event_game = functools.partial(self._controller.event_game, game)
            button = tk.Button(self._master, text=game, font=('Arial Bold', 40), command=event_game)
            button.pack(padx=200, pady=padding, fill=tk.X, anchor=tk.CENTER)

    def show_init_player(self, color):
        self._clear()
        label = tk.Label(self._master, text=color, font=('Arial Bold', 30))
        label.pack(padx=(30, 20), pady=20, anchor=tk.NW)

        for index, player in enumerate(['human', 'computer']):
            event_init_player = functools.partial(self._controller.event_init_player, player, color)
            button = tk.Button(self._master, text=player, font=('Arial Bold', 40), command=event_init_player)
            button.pack(padx=200, pady=10, fill=tk.X, anchor=tk.CENTER)

    def show_init_level(self, levels):
        self._clear()
        label = tk.Label(self._master, text='difficulity', font=('Arial Bold', 30))
        label.pack(padx=(30, 20), pady=20, anchor=tk.NW)

        level = tk.IntVar()
        scale = tk.Scale(self._master, variable=level, from_=1, to=levels, orient=tk.HORIZONTAL,
                         length=400, width=50, font=('Arial Bold', 30))
        scale.pack(pady=(10, 20), anchor=tk.CENTER)

        button = tk.Button(self._master, text='continue', font=('Arial Bold', 40),
                           command=lambda: self._controller.event_init_level(level.get()))
        button.pack(padx=200, fill=tk.X, anchor=tk.CENTER)
