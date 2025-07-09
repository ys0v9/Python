b,g=input().split(',')
g=int(g)
birthyear=int(b[:2])
if g%2==0:
    s='여성'
else:
    s='남성'

if g<3:
    age=2025-(birthyear+1900)+1
    print(f'현재나이 {age}살 {s}입니다.')
else:
    age=2025-(birthyear+2000)+1
    print(f'현재나이 {age}살 {s}입니다.')