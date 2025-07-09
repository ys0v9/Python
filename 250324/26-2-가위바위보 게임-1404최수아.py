import random as r

rsp = int(input('입력(1.가위 2.바위 3.보): '))

rsplist = ['가위', '바위', '보']

userChoice = rsplist[rsp - 1]

computerChoice = r.choice(rsplist)

if userChoice == computerChoice:
    print(f'user: {userChoice}  com: {computerChoice}  -> 비겼음')
elif (userChoice == '가위' and computerChoice == '보') or (userChoice == '바위' and computerChoice == '가위') or (userChoice == '보' and computerChoice == '바위'):
    print(f'user: {userChoice}  com: {computerChoice}  -> 이겼음')
else:
    print(f'user: {userChoice}  com: {computerChoice}  -> 졌음')