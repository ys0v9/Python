import math

# 입력
def f_input():
    lst = list(map(int, input().split()))
    return lst

# 평균
def f_avg(lst):
    mean = sum(lst) / len(lst)
    return mean

# 분산
def f_var(lst):
    mean = f_avg(lst)
    vsum = sum((x - mean) ** 2 for x in lst)
    var = vsum / len(lst)
    return var

# 표준편차
def f_std(lst):
    std = math.sqrt(f_var(lst))
    return std

# 최대공약수, 최소공배수
def f_comm(lst):
    gcd = math.gcd(*lst)
    lcm = math.lcm(*lst)
    return gcd, lcm

data = f_input()

print(f'평균: {f_avg(data)}')
print(f'분산: {f_var(data)}')
print(f'표준편차: {f_std(data)}')
gcd, lcm = f_comm(data)
print(f'최대공약수: {gcd}, 최소공배수: {lcm}')