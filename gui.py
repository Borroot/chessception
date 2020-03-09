from tkinter import *

# some random gui stuff
# https://www.edureka.co/blog/tkinter-tutorial

# label
# l1 = Label(window, text="edureka!", font=("Arial Bold", 50))
# l1.grid (column=0, row=0)

# txt = Entry(window, width=10)
# txt.grid(column=1, row=0)

# def clicked():
    # res = "LOL " + txt.get()
    # l1.configure(text= res)

# bt = Button (window, text="Enter", command=clicked)
# bt.grid(column=2, row=0)

def btn_click_start():
    print('hi')

def main():
    window = Tk()
    window.title("Chessception!")

    top_frame = Frame(window).pack()
    btn_start = Button(window, text="New Game", font=('Arial Bold', 50), command=btn_click_start).pack()

    window.geometry('800x400')
    window.mainloop()

if __name__ == "__main__":
    main()
