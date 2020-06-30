from controller.controller import Controller
from model.game.game import ResignException, DrawOfferException
from view.ui import Ui

import tkinter as tk
import functools
import sys


class Gui(Ui, tk.Frame):
    """
    This class provides a graphical user interface.
    """

    def __init__(self, mic, arm, unicode):
        self.background_colour = "White"
        self.button_colour = "DarkOrange1"

        self._master = tk.Tk()

        self._controller = Controller(self, mic, arm, unicode)
        self._controller.start()

        self._master.geometry("800x480")
        self._master.title("Chessception!")
        self._master.configure(bg=self.background_colour)

        self._master.mainloop()

    def _clear(self):
        for widget in self._master.winfo_children():
            widget.destroy()

    def request_game(self, games):
        self._clear()
        game_chosen = tk.StringVar()
        button = tk.Button(self._master, text="Quit", command=self._master.destroy, relief=tk.RIDGE, font=('Arial Bold', 15), bg=self.button_colour)
        button.pack(anchor=tk.NE)
        for index, game in enumerate(games):
            padding = (105, 10) if index == 0 else 10
            event_game = functools.partial(game_chosen.set, game)
            button = tk.Button(self._master, relief=tk.RIDGE, text=game.upper(), font=('Arial Bold', 30), bg=self.button_colour, command=event_game)
            button.pack(padx=200, pady=padding, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(game_chosen)
        return game_chosen.get()

    def request_player(self, name):
        self._clear()
        player_chosen = tk.StringVar()

        label = tk.Label(self._master, text=name.upper(), font=('Arial Bold', 25), bg=self.background_colour)
        label.pack(padx=(30, 20), pady=(20, 70), anchor=tk.NW)

        for index, player in enumerate(['human', 'computer']):
            event_player = functools.partial(player_chosen.set, player)
            button = tk.Button(self._master, text=player.upper(), font=('Arial Bold', 30), command=event_player, bg=self.button_colour)
            button.pack(padx=200, pady=10, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(player_chosen)
        return player_chosen.get()

    def request_level(self, levels):
        self._clear()
        label = tk.Label(self._master, text='DIFFICULTY', font=('Arial Bold', 25), bg=self.background_colour)
        label.pack(padx=(30, 20), pady=(20, 70), anchor=tk.NW)

        level_chosen = tk.IntVar()
        scale = tk.Scale(self._master, variable=level_chosen, from_=1, to=levels, orient=tk.HORIZONTAL,
                         length=400, width=50, font=('Arial Bold', 15))
        scale.pack(pady=(10, 10), anchor=tk.CENTER)

        done = tk.BooleanVar(False)
        button = tk.Button(self._master, text='CONTINUE', font=('Arial Bold', 30), command=lambda: done.set(True), bg=self.button_colour)
        button.pack(padx=200, fill=tk.X, anchor=tk.CENTER)

        self._master.wait_variable(done)
        return int(level_chosen.get())

    def request_move(self, game):
        self._master.grid_columnconfigure(0, weight=0, minsize=300)

        self.show_state(game.show_state())
        move_chosen = tk.StringVar()

        frame = tk.Frame(self._master, width=400, bg=self.background_colour)
        frame.grid(row=0, column=1, sticky="nsew")

        top_frame = tk.Frame(frame, bg=self.background_colour)
        top_frame.pack(padx=40, pady=(0, 60), anchor=tk.N)

        bottom_frame = tk.Frame(frame, bg=self.background_colour)
        bottom_frame.pack(padx=40, anchor=tk.S)

        text = tk.Text(top_frame, height=1, width=12, font=('Arial Bold', 30), bg = "snow2")
        text.grid(pady=20, row=0, column=0)

        button = tk.Button(top_frame, text='MOVE', font=('Arial Bold', 30), bg=self.button_colour, command=lambda: move_chosen.set(text.get('1.0', 'end-1c')))
        button.grid(row=1, column=0)

        button = tk.Button(bottom_frame, text='RESIGN', font=('Arial Bold', 30), bg=self.button_colour, command=lambda: move_chosen.set('resign'))
        button.grid(padx=20, row=1, column=0)

        button = tk.Button(bottom_frame, text='DRAW?', font=('Arial Bold', 30), bg=self.button_colour, command=lambda: move_chosen.set('draw?'))
        button.grid(padx=20, row=1, column=1)

        self._master.wait_variable(move_chosen)
        if move_chosen.get() == 'resign':
            raise ResignException()
        elif move_chosen.get() == 'draw?':
            raise DrawOfferException()
        return move_chosen.get()

    def request_draw(self):
        self._clear()
        label = tk.Label(self._master, text='A draw has been offered.', font=('Arial Bold', 40), bg=self.background_colour)
        label.pack(pady=30, anchor=tk.N)

        frame = tk.Frame(self._master, bg=self.background_colour)
        frame.pack(pady=60, anchor=tk.CENTER)

        accept = tk.BooleanVar()

        button = tk.Button(frame, text='ACCEPT', font=('Arial Bold', 30), bg=self.button_colour, command=lambda: accept.set(True))
        button.grid(padx=20, row=0, column=0)

        button = tk.Button(frame, text='DECLINE', font=('Arial Bold', 30), bg=self.button_colour, command=lambda: accept.set(False))
        button.grid(padx=20, row=0, column=1)

        self._master.wait_variable(accept)
        return accept.get()

    def show_state(self, state):
        self._clear()
        frame_board = tk.Frame(self._master, bg=self.background_colour)
        frame_board.grid(row=0, column=0, sticky="nsew")

        inner_frame = tk.Frame(frame_board, bg=self.background_colour)

        column = 1
        row = 1
        chess = (len(state) == 127)
        size = 14 if chess else 27
        pad1 = tk.Label(inner_frame, text="  " + chess*"  ", font=('Monospace', size), bg=self.background_colour)
        pad1.grid(padx=0, pady=0, row=0, column=0)

        for char in state:
            if char == '\n':
                row += 1
                column = 1
            else:
                if chess:
                    column += 1
                    label = tk.Label(inner_frame, text=char, font=('Monospace', size), bg=self.background_colour)
                else:
                    column += 2
                    label = tk.Label(inner_frame, text=char, font=('Monospace', size), width=4, height=2,
                                     bg=self.background_colour)
                label.grid(padx=0, pady=0, row=row, column=column)
        inner_frame.grid(row=0, column=0, sticky="")

    def show_message(self, message):
        self._clear()
        label = tk.Label(self._master, text=message, font=('Arial Bold', 20), bg=self.background_colour)
        label.pack(pady=30, anchor=tk.N)

        frame = tk.Frame(self._master, bg=self.background_colour)
        frame.pack(pady=60, anchor=tk.CENTER)

        okay = tk.BooleanVar()

        button = tk.Button(frame, text='OKAY', font=('Arial Bold', 30), bg=self.button_colour, command=lambda: okay.set(True))
        button.grid(padx=20, row=0, column=0)

        self._master.wait_variable(okay)
        return okay.get()

    def show_move_illegal(self, error):
        self.show_message(error)

    def show_speech_talk(self):
        self.show_message("Please talk into the microphone to communicate your move")

    def show_speech_error(self):
        self.show_message("Your speech was not recognized")

    def show_winner(self, winner):
        self._clear()

        text = "It's a draw!" if winner is None else '{0} has won!'.format(winner.__str__().title())
        label = tk.Label(self._master, text=text, font=('Arial Bold', 40), bg=self.background_colour)
        label.pack(pady=30, anchor=tk.N)

        done = tk.BooleanVar()
        button = tk.Button(self._master, text='MENU', font=('Arial Bold', 30), bg=self.button_colour, command=lambda: done.set(True))
        button.pack(pady=60, anchor=tk.CENTER)

        self._master.wait_variable(done)
