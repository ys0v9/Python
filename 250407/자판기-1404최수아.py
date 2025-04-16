juice = 5
while juice > 0:
    print('=' * 20)
    money = int(input('돈을 넣어주세요: '))

    change = money - 800

    if change > 0:
        print(f'맛있는 주스 드시고 잔돈 {change}원 받아 가세요.')
    elif change == 0:
        print('맛있는 주스 드세요.')
    else:
        print('가격을 확인하세요.')
        print(money)
        continue

    juice -= 1

print('주스가 매진되었습니다.')