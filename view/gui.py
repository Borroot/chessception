from tkinter import *

class Gui():
    """
    This class provides a graphical user interface for chessception.
    """

    def __init__(self):
        self.master = Tk()
        self.master.geometry("800x480")

        self.master.title("Chessception!")
        self.master.mainloop()

    # def screen_1():
        # pane = PanedWindow(self.master)
        # pane.pack(fill=BOTH, expand=1)

        # btn_start = Button(self.master, text="START", font=('Arial Bold', 80), command=btn_click_start).pack()
        # pane.add(btn_start)
