import time 

import customtkinter as tk

import datetime 

from tkinter import *

from tkinter import ttk

root = tk.CTk()

photo = PhotoImage(file="icon.png")

root.iconphoto(False, photo)

root.geometry("1400x100")

root.title("ReadingRuru")

root.resizable(width=True, height=False)



currenttime = datetime.datetime.now() 




label = tk.CTkLabel(root, text="Started at   "+str(currenttime))

label.configure(corner_radius=43)

label.pack(side=tk.BOTTOM)


root.mainloop()

