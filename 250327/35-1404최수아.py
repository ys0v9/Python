hap=0; count=0
while True:
    score=float(input())
    if score<0:
        print('음수가 입력되어서 프로그램을 종료합니다.')
        break
    else:
        hap+=score
        count+=1
print(f'합계: {hap}, 평균: {hap/count:.1f}')