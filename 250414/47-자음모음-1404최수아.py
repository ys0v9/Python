str=input()
print('#'*15)

con_c, vow_c = 0,0
con = 'bcdfghjklmnpqrstvwxyz'
vow = 'aeiou'

str.lower()

for i in str:
    if i in con:
        con_c += 1
    elif i in vow:
        vow_c += 1

print(f'자음 개수: {con_c}, 모음 개수: {vow_c}')