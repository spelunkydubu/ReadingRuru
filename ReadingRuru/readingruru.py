## Import different modules needed for application. 
import time 
import customtkinter as tk
import datetime 
from tkinter import *
from tkinter import ttk

## Establish a mainwindow.
root = tk.CTk()

## Get icon file. 
photo = PhotoImage(file="icon.png")

## Set icon file. 
root.iconphoto(False, photo)

## Set mainwindow gemoetry. 
root.geometry("1400x100")

## Set mainwndow title.
root.title("ReadingRuru")

## Disable resizable features for the x axis.
root.resizable(width=True, height=False)

## Get the time of the application startup.
currenttime = datetime.datetime.now() 

## Set a *label* for displaying the start up time.
label = tk.CTkLabel(root, text="Started at   "+str(currenttime))

## Makes the label rounded.(Does not show rounded in current config.)
label.configure(corner_radius=43)

## Set the label.
label.pack(side=tk.BOTTOM)

## Start the application loop.
root.mainloop()

