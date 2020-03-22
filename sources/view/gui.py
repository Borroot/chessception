from controller.controller import Controller
import tkinter as tk
import functools

# TODO Implement all of the functions in this class.
# NOTE Do not forget to implement the exceptions for move.
class Gui(tk.Frame):
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

    # def show_games(self, games):
    #     self._clear()
    #     for index, game in enumerate(games):
    #         padding = (100, 10) if index == 0 else 10
    #         event_game = functools.partial(self._controller.event_game, game)
    #         button = tk.Button(self._master, text=game, font=('Arial Bold', 40), command=event_game)
    #         button.pack(padx=200, pady=padding, fill=tk.X, anchor=tk.CENTER)

    def init_player(self, color):
        self._clear()
        label = tk.Label(self._master, text=color, font=('Arial Bold', 30))
        label.pack(padx=(30, 20), pady=20, anchor=tk.NW)

        player_chosen = tk.StringVar()
        for index, player in enumerate(['human', 'computer']):
            event_init_player = functools.partial(player_chosen.set, player)
            button = tk.Button(self._master, text=player, font=('Arial Bold', 40), command=event_init_player)
            button.pack(padx=200, pady=10, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(player_chosen)
        return player_chosen.get()

    # def init_level(self):
    #     self._clear()
    #     label = tk.Label(self._master, text='difficulity', font=('Arial Bold', 30))
    #     label.pack(padx=(30, 20), pady=20, anchor=tk.NW)
    #
    #     level = tk.IntVar()
    #     scale = tk.Scale(self._master, variable=level, from_=1, to=levels, orient=tk.HORIZONTAL,
    #                      length=400, width=50, font=('Arial Bold', 30))
    #     scale.pack(pady=(10, 20), anchor=tk.CENTER)
    #
    #     button = tk.Button(self._master, text='continue', font=('Arial Bold', 40),
    #                        command=lambda: self._controller.event_init_level(level.get()))
    #     button.pack(padx=200, fill=tk.X, anchor=tk.CENTER)

    # def show_state(state):
    #     self._clear()
    #     label = tk.Label(self._master, text=state, font=('Monospace', 20))
    #     label.pack(padx=40, pady=100, anchor=tk.W)

    def move(self, board):
        raise NotImplementedError("Please implement this method.")

    def info_illegal(self, move):
        raise NotImplementedError("Please implement this method.")
