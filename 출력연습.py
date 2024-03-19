name = "임정후"  # 파이썬은 데이터형이 없기 때문에 값이 대입될 때 결정됨
age = 31
gender = '남성'
jobs = "소프트웨어 개발자"
addr = "서울시 강남구"

# C언어 스타일 출력, %방식(서식을 지정함)
print("=" * 5)  # =를 5개 출력하라는 의미
print("=" * 5, "스타일 지정 방식", "=" * 5, sep="")
print("이름 : %s" % name)
print("나이 : %d, 성별 : %s" % (age, gender))  # 나이 : 31, 성별 : 남성
print("직업 : %s" % jobs)
print("주소 : %s" % addr)

# 파이썬 3.6 이전 스타일
print("=" * 5, "3.6 이전 스타일", "=" * 5, sep="")
print("이름 : {}".format(name))
print("이름 : {} {}".format(name,addr))

# 파이썬 현재 스타일
print("=" * 5, "파이썬 현재 스타일", "=" * 5, sep="")
print(f"이름 : {name}")
print(f"성별 : {gender}, 직업 : {jobs}, 나이 : {age}")