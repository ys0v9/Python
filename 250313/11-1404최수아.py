student=['홍길동','일지매']
print(f'현재 프로그래밍 수강 신청자는 {student}입니다.')
plus=input('추가할 학생 이름: ')
print(f'{plus} 학생의 신청이 완료되었습니다.')
student.append(plus)
print(f'현재 이 과목의 최종 신청자는 {student}입니다.')

wd = input('철회할 학생 이름: ')
if wd in student:
    student.remove(wd)
    print(f'{wd} 학생의 수강 철회가 완료되었습니다.')
else:
    print(f'{wd} 학생은 현재 수강 신청자 목록에 없습니다.')
print(f'현재 이 과목의 최종 신청자는 {student}입니다.')

old_name=input('변경 전 이름: ')
if old_name in student:
    new_name = input(f'{old_name} 변경 후 이름: ')
    student[student.index(old_name)] = new_name
    print(f'요청하신 대로 {old_name}를 {new_name}(으)로 변경하였습니다.')
else:
    print(f'{old_name} 학생은 현재 수강 신청자 목록에 없습니다.')

print(f'현재 이 과목의 최종 신청자는 {student}입니다.')