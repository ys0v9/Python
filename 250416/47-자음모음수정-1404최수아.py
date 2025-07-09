# sen = input()
# eng = 0
# num = 0
# spa = 0
# oth = 0
# for i in sen:
#     if i.isalpha():
#         eng += 1
#     elif i.isdigit():
#         num += 1
#     elif i.isspace():
#         spa += 1
#     else:
#         oth += 1
# print(eng, num, spa, oth)

str=input()
print('#'*15)

con_c, vow_c = 0,0
con = 'bcdfghjklmnpqrstvwxyz'
vow = 'aeiou'

str.lower()

for j in str:
    if j.isalpha():
        if j in vow:
            vow_c += 1
        else:
            con_c += 1


print(f'자음 개수: {con_c}, 모음 개수: {vow_c}')