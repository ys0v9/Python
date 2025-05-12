# 사용자로부터 이름, 나이, 학교 입력받아 me.txt에 저장

name = input("이름: ")
age = input("나이: ")
school = input("학교: ")

f = open("me.txt", "w")

f.write(f'이름: {name}, 나이: {age}, 학교: {school}')