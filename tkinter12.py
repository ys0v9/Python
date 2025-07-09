from tkinter import *

root = Tk()
root.title("배치관리자")
root.geometry("300x200")

btn_1 = Button(root, text = "Button1", bg = "green")
btn_2 = Button(root, text = "Button2", bg = "red")
btn_3 = Button(root, text = "Button3", bg = "blue")
btn_4 = Button(root, text = "Button4", bg = "yellow")
btn_5 = Button(root, text = "Button5", bg = "pink")
btn_6 = Button(root, text = "Button6", bg = "purple")
btn_7 = Button(root, text = "Button7", bg = "gold")

btn_1.pack(side="left")
btn_2.pack(side="left")
btn_3.pack(side="left")
btn_4.pack()
btn_5.pack(side="bottom")
btn_6.pack(side="right")

root.mainloop()