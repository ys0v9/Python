from turtle import *
import random as r # 먹이 랜덤 위치 이동

# 스크린도 객체

# 등장인물 만들기
# 하나만 만들 때는 객체 따로 안만들어도 t. 쓰면 가능
tc = Turtle() # 주인공 거북(흰색)
tc.shape("turtle")
tc.color("white")
tc.up()
tc.speed(0)


# 악당 객체 생성
tv = Turtle() # 악당 거북(빨간색)
tv.shape("turtle")
tv.color("red")
tv.speed(0)
tv.up()
tv.goto(0, 200)


# 먹이 객체 생성
tf = Turtle() # 먹이(초록색 원)
tf.shape("circle")
tf.color("green")
tf.up()
tf.goto(0, -200) # 먹이 시작 위치


# 주인공 움직임 정의 (키보드 방향키)
def turn_right():
    tc.setheading(0) # seth 까지 써도 가능 # 절대 각도 0: 오른쪽
    
def turn_left():
    tc.setheading(180)
    
def turn_up():
    tc.setheading(90)
    
def turn_down():
    tc.setheading(270)


# play 함수
def play():
    tc.fd(10) # 주인공 앞으로 이동
    ang = tv.towards(tc.pos()) # 악당입장, 주인공 위치의 상대 각도 
    tv.setheading(ang) # 악당이 주인공 쪽을 바라보게
    tv.fd(9) # 악당 앞으로 이동

    if tc.distance(tf) < 12: # 주인공과 먹이 거리가 가까우면
        start_x = r.randint(-230, 230)
        start_y = r.randint(-230, 230)
        tf.goto(start_x, start_y) # 먹이를 다른 곳으로 이동

    if tc.distance(tv) >= 12: # 주인공과 악당 거리가 멀면
        ontimer(play, 100) # 0.1초 후 play 함수 실행(게임 계속)
    

# 게임 준비
def ready():
    setup(500, 500) # 화면 크기
    title("Turtle Run") # 창 제목
    bgcolor("orange") # 배경 색


# 이벤트에 따른 움직임 설정
def move():
    onkeypress(turn_right, "Right")
    onkeypress(turn_left, "Left")
    onkeypress(turn_up, "Up")
    onkeypress(turn_down, "Down")
    onkeypress(play, "space") #space키 눌러서 게임 시작


# 메인
ready() # 게임 준비
move() # 시작
listen() # 이벤트 감지

exitonclick()
