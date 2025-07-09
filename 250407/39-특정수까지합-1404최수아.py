#39-1
n=int(input())
s=0
for i in range(n+1):
    s+=i
print(f'1부터 {n}까지의 합은 {s}')

#39-2
a=int(input('자연수 입력: '))
b=1
for i in range(1,a+1):
    b*=i
print(f'{a}!은 {b}')