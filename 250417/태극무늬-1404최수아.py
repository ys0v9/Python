from turtle import *

shape("turtle")
bgcolor("black")
pensize(2)
speed(0)

x = 1

for i in range(200):
    if i % 3 == 0:
        color("red")
    elif i % 3 == 1:
        color("yellow")
    else:
        color("blue")
        
    fd(x)
    lt(119)
    
    x += 2 
    
done()