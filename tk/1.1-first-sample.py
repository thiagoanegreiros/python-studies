import tkinter as tk
from tkinter import messagebox

def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy();

skylight = tk.Tk()
skylight.title("Skylight")

button = tk.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)

skylight.mainloop()
