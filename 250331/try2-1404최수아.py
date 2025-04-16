while True:
    n=input()
    if n=='q':
        print('q가 입력되어서 프로그램을 종료합니다.')
        break

    try:
        num=int(n)
    except ValueError:
        print('숫자를 입력해주세요: ')
        continue

    if num==0:
        print('0은 5의 배수가 아닙니다.')
    elif num%5==0:
        print(f'{num}은 5의 배수입니다.')
    else:
        print(f'{num}은 5의 배수가 아닙니다.')