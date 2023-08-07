from tkinter import *
from tkinter.ttk import Combobox,Checkbutton,Radiobutton

window = Tk()
# 设置标题
window.title("First Window")
# 设置窗口大小
# window.geometry("500x200")
# 添加 label 标签
lbl = Label(window, text="Hello World", font=("Arial Bold", 50))
# grid 格子 函数设置其在窗口的位置
lbl.grid(column=0, row=0)
# Entry 入口 输入框
txt = Entry(window, width=10)
txt.grid(column=0,row=1)
# 加入输入框的聚焦
txt.focus()
def clicked():
    res="Welcome to "+txt.get()+" : "+combo.get()
    lbl.configure(text=res)

# 添加 btn 按钮组件
btn = Button(window, text="Click Me",bg="orange",fg="white",command=clicked)
# 设置按钮在窗口的位置
btn.grid(column=0, row=4)

combo=Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(2)
combo.grid(column=0, row=3)


var = IntVar() # 初始化值 好东西
# 这里是预设值 这里注意到的是 关于Checkbutton var的预设值 必须唯一 否者 达不到效果
chk_state = BooleanVar()
chk_state.set(True) # Set check state
chk = Checkbutton(window, text="苹果", variable=var)
chk1 = Checkbutton(window, text="香蕉", var=True)
chk2 = Checkbutton(window, text="橘子", var=False)
chk.grid(column=1, row=5)
chk1.grid(column=2, row=5)
chk2.grid(column=3, row=5)

rad1 = Radiobutton(window, text="First", value=1)
rad2 = Radiobutton(window, text="Second", value=2)
rad3 = Radiobutton(window, text="Third", value=3)
rad1.grid(column=1, row=6)
rad2.grid(column=2, row=6)
rad3.grid(column=3, row=6)


# 显示窗口
window.mainloop()
