from tkinter import *

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Chessception!")

        pane = PanedWindow(self.master)
        pane.pack(fill=BOTH, expand=1)

        btn_start = Button(self.master, text="START", font=('Arial Bold', 80), command=btn_click_start).pack()
        pane.add(btn_start)

    def


def main():
    master = Tk()
    master.geometry("800x480")

    app = Window(master)
    master.mainloop()

if __name__ == "__main__":
    main()
