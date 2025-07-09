from turtle import *

t = Turtle()
t.shape("turtle")
t.color("pink", "skyblue")
t.pensize(3)

t.penup()
t.goto(-200, 200)
t.pendown()

t.begin_fill()
for i in range(4):
    t.fd(200)
    t.rt(90) 
t.end_fill()

t.penup()
t.goto(100,100)
t.pendown()

for j in range(3):
    t.fd(100)
    t.lt(120)
    