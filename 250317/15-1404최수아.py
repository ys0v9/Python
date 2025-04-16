stu1={'학반':105,'번호':20,'이름':'홍길동'}
#키로 값 찾기
print(stu1['학반'])
print(stu1['번호'])
print(stu1['이름'])

#키로 값에 접근
print(stu1.get('이름'))

#차이점
# print(stu1.get('주소'))
# print(stu1['주소'])

#딕셔너리의 모든 키 반환
print(stu1.keys())
print(list(stu1.keys()))

#딕셔너리의 모든 값 반환
print(stu1.values())
print(list(stu1.values()))

#딕셔너리 안에 키가 있는지 확인
print('이름' in stu1)
print('주소' in stu1)