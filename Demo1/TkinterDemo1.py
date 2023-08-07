from tkinter import *
from tkinter import messagebox,ttk
from tkinter.ttk import Progressbar

window = Tk()
window.title("First Window")
window.geometry("350x200")
def clicked():
    res="Message content_"+spin.get()
    messagebox.showinfo("Message title", res)
btn = Button(window, text="Click here", command=clicked)
btn.grid(column=0, row=0)

# 初始值0
var=IntVar()
# 设置预设值
var.set(36)
spin=Spinbox(window,from_=0,to=100,width=5,textvariable=var)
spin.grid(column=0,row=1)

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 10
bar.grid(column=0, row=2)

window.mainloop()