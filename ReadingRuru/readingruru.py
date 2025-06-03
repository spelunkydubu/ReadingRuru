import time 

import tkinter as tk

import datetime 

from tkinter import *

from tkinter import ttk

root = Tk()

photo = PhotoImage(file="icon.png")

root.iconphoto(False, photo)

root.geometry("1400x100")

root.title("ReadingRuru")

print("Please choose your desired colour , white or black?")

getcolor = input()

root.configure(bg=str(getcolor))

root.resizable(width=True, height=False)



currenttime = datetime.datetime.now() 




label = tk.Label(root, text="Started at   "+str(currenttime))

label.config(bg="grey")

label.pack(side=tk.BOTTOM)


root.mainloop()

