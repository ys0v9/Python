import random as r
import time

w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
n = 0  
total = 0

print('[타자게임] 준비되면 엔터')
input()
start = time.time()

while n < 5:
    q = r.choice(w)
    print(f'[문제 {n+1}]')
    print(q)  
    ans = input()
    total += 1  
    if q == ans:
        print('pass')
        n += 1
    else:
        print('틀렸습니다.')

end = time.time()
re = end - start
print('-------------------------')
print(f'총 문제 {total}개 중에 5개 맞았습니다.')
print(f'걸린 시간: {re}초')