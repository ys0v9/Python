#반복문으로 파일에 한 줄씩 쓰기
f = open("data_2.txt", "w")

for i in range(1,11):
    line = input()
    f.write(f"{line}\n")

f.close()
print("정상 종료")