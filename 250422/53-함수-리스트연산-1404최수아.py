def lst_create():
    lst = list(map(float, input('숫자(공백으로 분리): ').split()))
    return lst

def lst_append(lst):
    while True:
        p = input('추가 숫자: ')
        try:
            a_p = float(p)
            lst.append(a_p)
        except ValueError:
            break
    return lst

def lst_cal(lst):
    total = sum(lst)
    avg = total / len(lst)
    return total, avg

def lst_print(lst, total, avg):
    print(f"점수: {lst}")
    print(f"합계: {total:.2f}  평균: {avg:.2f}")


#main
print("*** 리스트 생성")
lst = lst_create()

print("*** 숫자 추가(문자 입력 시 추가 종료)")
lst = lst_append(lst)

print('*** 계산 결과')
total, avg = lst_cal(lst)

lst_print(lst, total, avg)