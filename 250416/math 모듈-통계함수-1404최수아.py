import math

lst = list(range(1, 11))
print(lst)

#평균
mean = sum(lst) / len(lst)
print(f'평균: {mean}')

#분산
vsum = 0 
for x in lst:
    vsum += (x - mean) ** 2
var = vsum / len(lst)
print(f'분산: {var}')

#표준편차
std = math.sqrt(var)
print(f'표준편차: {std}')

#최대공약수, 최소공배수
gcd = math.gcd(*lst)
lcm = math.lcm(*lst)
print(f'최대공약수: {gcd}, 최소공배수: {lcm}')