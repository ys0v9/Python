from tkinter import *

def print_1():
    button1["text"] = "버튼1이 클릭됨"

def print_2():
    button2["text"] = "버튼2가 클릭됨"

window = TK()

lbl1 = Label(window, "레이블 입니다.")
button1 = Button(window, text = "1번 버튼입니다.")
button2 = Button(window, text = "2번 버튼입니다.")
lbl1.pack()
button1.pack(side = LEFT, padx = 10)
button2.pack(side = LEFT, padx = 10)


window.mainloop()