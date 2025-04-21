import math

#평균
def f_avg(lst):
    mean = sum(lst) / len(lst)
    return (mean)

#분산
def f_var(lst):
    vsum=0
    for x in lst:
        vsum += (x-f_avg(lst)) ** 2
    var = vsum / len(lst)
    return (var)

#표준편차
def f_std(lst):
    std = math.sqrt(f_var(lst))
    return (std)

#최대공약수, 최소공배수
def f_comm(lst):
    gcd = math.gcd(*lst)
    lcm = math.lcm(*lst)
    return gcd, lcm

lst = list(map(int,input().split()))
print(f'평균: {f_avg(lst)}')
print(f'분산: {f_var(lst)}')
print(f'표준편차: {f_std(lst)}')
print(f'최대공약수, 최소공배수: {f_comm(lst)}')