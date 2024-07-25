import time

print("Hello, Python !!!!")
print(100)
print(100+200)

name = "임어부" # 파이썬은 데이터 타입이 없음
print(name)

# <- 주석

name = "임정후"
email = "dlaeocjf94@naver.com"
position = "학생"
addr = "서울시 강남구 역삼동 KH 정보 교육원"

# """ """ / ''' ''' 여러 줄 쓰는것
print(f"""
주소 : {addr}
직책 : {position}
이름 : {name}
이메일 : {email}
""")

if True:
    print("정상")
else:
    print("에러")

# 전체 주석 잡기 (or ''' ''')
"""
작성자 : 임정후
목적 : 파이썬 연습용 프로그램
날짜 : 2024.03.18
"""

print(38) # 숫자를 출력
print("문자열 출력")
print([1,2,3])
print(["리","스","트","출","력"])

# [] : 리스트를 표시, {} : 딕셔너리 표시, () : 함수의 인수, 튜플


