#38-1
n=int(input('어디까지 출력할까요?: '))
for i in range(n):
    print(i+1)

#38-2
nu=int(input("어디부터 출력할까요?: "))
for j in range(n,-1,-1):
    print(j)

#38-3
num=int(input("몇 단? "))
print(f'=== {num}단 ===')
for k in range(1,10):
    print(f'{num} * {k} = {num*k}')