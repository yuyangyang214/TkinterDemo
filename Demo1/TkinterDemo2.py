from tkinter import *
from tkinter import filedialog,messagebox
import os

window = Tk()
window.title("First Window")
window.geometry('350x200')
def clicked():
    file = filedialog.askopenfilenames(initialdir=os.path.dirname(__file__))
    messagebox.showinfo("Message title", file)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=0)
window.mainloop()