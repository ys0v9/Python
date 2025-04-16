# #예외처리
# a=4
# b=0
# try:
#     c=a/b
# except ZeroDivisionError:
#     pass

while True:
    print("##예외 처리 1##")
    try:
     n_1 = int(input('숫자: '))
    except ValueError:
      print('숫자만 입력하세요.')
      continue
    else:
      print(n_1)
      break