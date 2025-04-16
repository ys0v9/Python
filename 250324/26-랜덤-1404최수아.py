import random as r

#0이상 1미만 실수 중 난수 생성
print(r.random()) 

#10이상 11미만 실수 중 난수 생성
print(r.uniform(10,11)) 

#10이상 100이하 정수 중 난수 생성
print(r.randint(10,100)) 

#10이상 100미만 10간격 정수 리스트 중 임의의 수 추출
print(r.randrange(10,100,10)) 

#1이상 10미만 1간격 정수 리스트 생성
a_list=list(range(1,10))

#a_list에서 임의의 수 출력
print(r.choice(a_list))

#a_list에서 난수 3개 추출(중복 허용)
print(r.choices(a_list,k=3))

#a_list에서 중복되지 않는 난수 2개 리스트로 출력
print(r.sample(a_list,k=2)) 

teacher=['마아람','정다혜','강진아','이승호']

#teacher 리스트 요소의 순서 임의로 변경하여 출력
r.shuffle(teacher)
print(teacher)