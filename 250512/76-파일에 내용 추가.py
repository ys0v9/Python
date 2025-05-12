# 파일에 내용 추가
f = open("data_2.txt", "a")

for i in range(11, 21):
    content = input()
    f.write(f'{content}\n')
    
f.close()