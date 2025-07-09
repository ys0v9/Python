import random as r

userInput = list(map(int, input('2개 입력(1~6, 중복 허용): ').split()))
dice = [r.randint(1, 6), r.randint(1, 6)]

print(f"Com: {dice}")
print(f'User: {userInput}')

if sorted(dice) == sorted(userInput):
    print("1등")
elif userInput[0] in dice or userInput[1] in dice:
    print("2등")
else:
    print("3등")