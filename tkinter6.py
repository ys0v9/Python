from tkinter import *
window = Tk()

lbl1 = Label(window, text="이것은 레이블입니다.")
btn1 = Button(window, text = "1번 버튼입니다.")
btn2 = Button(window, text = "2번 버튼입니다.")
lbl1.pack() 
btn1.pack(side = LEFT, padx = 10)
btn2.pack(side = LEFT, padx = 10)

window.mainloop()