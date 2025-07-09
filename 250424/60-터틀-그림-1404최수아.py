from turtle import *
t = 'turtle'

d = 10
f = 30

def turn_right():
    setheading(0); fd(d); color('salmon'); pensize(5)

def turn_up():
    setheading(90); fd(d); color('salmon'); pensize(5)

def turn_left():
    setheading(180); fd(d); color('salmon'); pensize(5)

def turn_down():
    setheading(270); fd(d); color('salmon'); pensize(5)


def turn_right1():
    setheading(0); fd(f); color('salmon'); pensize(20)

def turn_up1():
    setheading(90); fd(f); color('salmon'); pensize(20)

def turn_left1():
    setheading(180); fd(f); color('salmon'); pensize(20)

def turn_down1():
    setheading(270); fd(f); color('salmon'); pensize(20)



 

def blank():
    clear()

def keyboard():
    shape('turtle')
    speed(0)
    onkeypress(turn_right, "d")
    onkeypress(turn_up, "w")
    onkeypress(turn_left, "a")
    onkeypress(turn_down, "s")

    onkeypress(turn_right1, "D")
    onkeypress(turn_up1, "W")
    onkeypress(turn_left1, "A")
    onkeypress(turn_down1, "S")
    onkeypress(blank, "Escape")
    listen()


def mouse():
    speed(0)
    pensize(2)
    onscreenclick(goto)
    onkeypress(blank, "Escape")
    listen()

select = input("키보드(1) 마우스(2): ")

if select == "1":
    keyboard()
elif select == "2":
    mouse()