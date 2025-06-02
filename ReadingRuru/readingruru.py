from tkinter import *

from tkinter import ttk

root = Tk()

root.geometry("1400x100")

root.title("readingruru")

print("Please choose your desired colour , white or black?")

getcolor = input()

root.configure(bg=str(getcolor))

root.resizable(width=True, height=False)

root.mainloop()

