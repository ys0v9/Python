from turtle import *

shape("turtle")
color("black", "brown")
pensize(3)

#한 변의 길이와 도형 종류 입력
def input_data():
    x, y = map(int,input("종류(3이상) 한변(5이상): ").split())
    #데이터 이상 체크 후
    return x, y

#이동 함수
def moving():
    a,b = map(int,input('이동할 좌표(a b): ').split()) #이동할 좌표 입력
    #이동
    up()
    goto(a,b)
    down()

#도형 그리기
def polygon():
    n,a=input_data() #입력
    #도형그리기
    begin_fill()
    for i in range(n):
        fd(a)
        lt(360/n)
    end_fill()

#Main
while True:
    print("===도형 그리기===")
    moving()
    polygon()

    con = int(input("계속(y(1) n(그 외): "))
    if con != 1:
        break

exitonclick()
