from controller.controller import Controller
from view.ui import Ui

import tkinter as tk
import functools


class Gui(Ui, tk.Frame):
    """
    This class provides a graphical user interface.
    """

    def __init__(self, mic, arm):
        self._master = tk.Tk()
        tk.Frame.__init__(self, self._master)

        self._controller = Controller(self, mic, arm)
        self._controller.start()

        self._master.geometry("800x480")
        self._master.title("Chessception!")
        self._master.mainloop()

    def _clear(self):
        for widget in self._master.winfo_children():
            widget.destroy()

    def request_game(self, games):
        self._clear()
        game_chosen = tk.StringVar()

        for index, game in enumerate(games):
            padding = (100, 10) if index == 0 else 10

            event_game = functools.partial(game_chosen.set, game)
            button = tk.Button(self._master, text=game, font=('Arial Bold', 40), command=event_game)
            button.pack(padx=200, pady=padding, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(game_chosen)
        return game_chosen.get()

    def request_player(self, color):
        self._clear()
        player_chosen = tk.StringVar()

        label = tk.Label(self._master, text=color, font=('Arial Bold', 30))
        label.pack(padx=(30, 20), pady=20, anchor=tk.NW)

        for index, player in enumerate(['human', 'computer']):
            event_player = functools.partial(player_chosen.set, player)
            button = tk.Button(self._master, text=player, font=('Arial Bold', 40), command=event_player)
            button.pack(padx=200, pady=10, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(player_chosen)
        return player_chosen.get()

    def request_level(self, levels):
        self._clear()
        label = tk.Label(self._master, text='difficulity', font=('Arial Bold', 30))
        label.pack(padx=(30, 20), pady=20, anchor=tk.NW)

        level_chosen = tk.IntVar()
        scale = tk.Scale(self._master, variable=level_chosen, from_=1, to=levels, orient=tk.HORIZONTAL,
                         length=400, width=50, font=('Arial Bold', 30))
        scale.pack(pady=(10, 20), anchor=tk.CENTER)

        done = tk.BooleanVar(False)
        button = tk.Button(self._master, text='continue', font=('Arial Bold', 40), command=lambda: done.set(True))
        button.pack(padx=200, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(done)
        return int(level_chosen.get())

    def request_move(self, board):
        # NOTE Do not forget to implement the exceptions for move.
        raise NotImplementedError("Please implement this method.")

    def show_state(self, state):
        self._clear()
        label = tk.Label(self._master, text=state, font=('Monospace', 20))
        label.pack(padx=40, pady=100, anchor=tk.W)

