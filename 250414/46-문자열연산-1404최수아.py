str = input('문장 입력: ')
print('#'*20)
print(f'대문자 변환: {str.upper()}')
print(f'소문자 변환: {str.lower()}')
print(f'문자열 길이: {len(str)}')
print(f'공백으로 분리: {str.split()}')
print(f'문자로 분리: {str.split(",")}')
print(f"o의 위치: {str.find('o')}")
print(f"o의 개수: {str.count('o')}")
print(f"Python을 AI로 교체: {str.replace('Python','AI')}")