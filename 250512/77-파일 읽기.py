# 파일 내용 읽어 화면에 출력
# read()
f = open("data_2.txt", "r")
content = f.read() # 내용 전체
print(content)
f.close()