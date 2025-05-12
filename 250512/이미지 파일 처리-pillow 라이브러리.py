# 이미지 모듈 호출
from PIL import Image

# 이미지 열기
img = Image.open("39a1df6c-0d2b-419e-aeb3-5037e038784a.jpeg") # 같은 폴더에 있는 이미지
img.show() # 기본 이미지 뷰어로 열기

# 이미지 정보 확인
print("이미지 크기:", img.size) # 크기는 튜플형(가로, 세로)
print("이미지 형식:", img.format) # 등
print("이미지 모드:", img.mode) # 등