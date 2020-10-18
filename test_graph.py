from view.window import Window
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    root.geometry("350x100+300+300")
    app = Window()
    root.mainloop()