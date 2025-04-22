import random

#함수 정의(문자열도 choice 가능)
def genPass():
    chr="abcdefghijklmnopqrstuvwxyz0123456789"
    passwd = ""
    for i in range(8):
        ch =random.choice(chr)
        passwd += ch
    return passwd

#main
for i in range(3):
    result = genPass()
    print(f"암호 {i+1}: \033[31m {result} \033[0m") 