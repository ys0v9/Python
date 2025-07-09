from turtle import *

n = int(input("몇 각형?: "))
f = int(input("한 변의 길이: "))

shape ("turtle")

color("black","brown")

pensize(3)

begin_fill()
for i in range(n):
    fd(f)
    lt(360//n)
end_fill()
