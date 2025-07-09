while True:
    n=int(input())
    if n==0:
        print('0이 입력되어서 프로그램을 종료합니다.')
        break
    elif n%5==0:
        print(f'{n}은 5의 배수입니다.')
        continue
    print(f'{n}은 5의 배수가 아닙니다.')