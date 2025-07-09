from tkinter import *

root = Tk()
root.geometry("300x200")

top_btn = Button(root, text="Top")
top_btn.pack(side="top", fill="x")

bottom_btn = Button(root, text="Bottom")
bottom_btn.pack(side="bottom", fill="x")

left_btn = Button(root, text="Left")
left_btn.pack(side="left", fill="y")

right_btn = Button(root, text="Right")
right_btn.pack(side="right", fill="y")

center_lbl = Label(root, text="Center Area", bg="lightgray")
center_lbl.pack(expand=True, fill="both")

root.mainloop()