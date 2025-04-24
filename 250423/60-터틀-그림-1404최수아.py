from turtle import *
d = 10
p = 30

def turn_right():
    setheading(0) ; fd(d) ; color("red") ; pensize(3)

def turn_left():
    setheading(180) ; fd(d) ; color("yellow") ; pensize(3)

def turn_up():
    setheading(90) ; fd(d) ; color("blue") ; pensize(3)

def turn_down():
    setheading(270) ; fd(d) ; color("green"); pensize(3)

def turn_right1():
    setheading(0) ; fd(p) ; color("medium orchid") ; pensize(15)

def turn_left1():
    setheading(180) ; fd(p) ; color("deep sky blue") ; pensize(15)

def turn_up1():
    setheading(90) ; fd(p) ; color("light coral") ; pensize(15)

def turn_down1():
    setheading(270) ; fd(p) ; color("pale green") ; pensize(15)

def blank():
    clear()

def keyboard():
    shape("turtle")
    speed(50)
    onkeypress(turn_right, "d")
    onkeypress(turn_left, "a")
    onkeypress(turn_up, "w")
    onkeypress(turn_down, "s")
    onkeypress(blank, "Escape")
    onkeypress(turn_right1, "D")
    onkeypress(turn_left1, "A")
    onkeypress(turn_up1, "W")
    onkeypress(turn_down1, "S")
    listen()

def mouse():
    speed(0)
    pensize(2)
    ondrag(goto)
    onkeypress(blank, "Escape")
    listen()

# main
select = input("키보드(1) 마우스(2): ")
if select == "1":
    keyboard()
elif select == "2":
    mouse()
