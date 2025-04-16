fruit=[]
while True:
    a=input()
    if a in fruit:
        print('이미 있습니다.')
    else:
        fruit.append(a)
        print(fruit)
    if len(fruit)==5:
        print('프로그램 종료')
        break