from controller.controller import Controller
from model.game.game import ResignException, DrawOfferException
from view.ui import Ui

import tkinter as tk
import functools


class Gui(Ui, tk.Frame):
    """
    This class provides a graphical user interface.
    """
    # TODO: Add a button to close the window.

    def __init__(self, mic, arm, unicode):
        self._master = tk.Tk()
        tk.Frame.__init__(self, self._master)

        self._controller = Controller(self, mic, arm, unicode)
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
            padding = (150, 10) if index == 0 else 10

            event_game = functools.partial(game_chosen.set, game)
            button = tk.Button(self._master, text=game.upper(), font=('Arial Bold', 30), command=event_game)
            button.pack(padx=200, pady=padding, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(game_chosen)
        return game_chosen.get()

    def request_player(self, name):
        self._clear()
        player_chosen = tk.StringVar()

        label = tk.Label(self._master, text=name.upper(), font=('Arial Bold', 25))
        label.pack(padx=(30, 20), pady=(20, 70), anchor=tk.NW)

        for index, player in enumerate(['human', 'computer']):
            event_player = functools.partial(player_chosen.set, player)
            button = tk.Button(self._master, text=player.upper(), font=('Arial Bold', 30), command=event_player)
            button.pack(padx=200, pady=10, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(player_chosen)
        return player_chosen.get()

    def request_level(self, levels):
        self._clear()
        label = tk.Label(self._master, text='DIFFICULTY', font=('Arial Bold', 25))
        label.pack(padx=(30, 20), pady=(20, 70), anchor=tk.NW)

        level_chosen = tk.IntVar()
        scale = tk.Scale(self._master, variable=level_chosen, from_=1, to=levels, orient=tk.HORIZONTAL,
                         length=400, width=50, font=('Arial Bold', 15))
        scale.pack(pady=(10, 10), anchor=tk.CENTER)

        done = tk.BooleanVar(False)
        button = tk.Button(self._master, text='CONTINUE', font=('Arial Bold', 30), command=lambda: done.set(True))
        button.pack(padx=200, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(done)
        return int(level_chosen.get())

    def request_move(self, game):
        self.show_state(game.show_state())
        move_chosen = tk.StringVar()

        frame = tk.Frame(self._master)
        frame.grid(row=0, column=1)

        top_frame = tk.Frame(frame)
        top_frame.pack(padx=40, pady=(0, 60), anchor=tk.N)

        bottom_frame = tk.Frame(frame)
        bottom_frame.pack(padx=40, anchor=tk.S)

        text = tk.Text(top_frame, height=1, width=12, font=('Arial Bold', 30))
        text.grid(pady=20, row=0, column=0)

        button = tk.Button(top_frame, text='MOVE', font=('Arial Bold', 30), command=lambda: move_chosen.set(text.get('1.0', 'end-1c')))
        button.grid(row=1, column=0)

        button = tk.Button(bottom_frame, text='RESIGN', font=('Arial Bold', 30), command=lambda: move_chosen.set('resign'))
        button.grid(padx=20, row=1, column=0)

        button = tk.Button(bottom_frame, text='DRAW?', font=('Arial Bold', 30), command=lambda: move_chosen.set('draw?'))
        button.grid(padx=20, row=1, column=1)

        self._master.wait_variable(move_chosen)
        if move_chosen.get() == 'resign':
            raise ResignException()
        elif move_chosen.get() == 'draw?':
            raise DrawOfferException()
        return move_chosen.get()

    def request_draw(self):
        self._clear()
        label = tk.Label(self._master, text='A draw has been offered.', font=('Arial Bold', 40))
        label.pack(pady=30, anchor=tk.N)

        frame = tk.Frame(self._master)
        frame.pack(pady=60, anchor=tk.CENTER)

        accept = tk.BooleanVar()

        button = tk.Button(frame, text='ACCEPT', font=('Arial Bold', 30), command=lambda: accept.set(True))
        button.grid(padx=20, row=0, column=0)

        button = tk.Button(frame, text='DECLINE', font=('Arial Bold', 30), command=lambda: accept.set(False))
        button.grid(padx=20, row=0, column=1)

        self._master.wait_variable(accept)
        return accept.get()

    def show_state(self, state):
        self._clear()
        # TODO: Show the state monospaced when using unicode characters.
        # TODO: Make the size depended on the number of characters, i.e. for tic tac toe it will be bigger than for chess.
        label = tk.Label(self._master, text=state, font=('Monospace', 17))
        label.grid(padx=40, pady=90, row=0, column=0)

    def show_move_illegal(self, error):
        # TODO: Show the error message.
        pass

    def show_speech_talk(self):
        # TODO: Show that the user has to talk in the microphone to give his move.
        pass

    def show_speech_error(self):
        # TODO: Show that the speech was not recognised.
        pass

    def show_winner(self, winner):
        self._clear()

        text = "It's a draw!" if winner is None else '{0} has won!'.format(winner.__str__().title())
        label = tk.Label(self._master, text=text, font=('Arial Bold', 40))
        label.pack(pady=30, anchor=tk.N)

        done = tk.BooleanVar()
        button = tk.Button(self._master, text='MENU', font=('Arial Bold', 30), command=lambda: done.set(True))
        button.pack(pady=60, anchor=tk.CENTER)

        self._master.wait_variable(done)
