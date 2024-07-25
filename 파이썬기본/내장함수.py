# 내장 함수 : 별도의 import 없이 사용 할 수 있도록 내장된 함수
print(max(10, 2, 32, 45, 4, 49))
print(min(10, 2, 32, 45, 4, 49))

# sum은 리스트 혹은 튜플 형태로 전달
print(sum([26, 34, 45, 67, 67]))
value = 1,2,3,4,5,6,7,8,9,10
print(sum(value))
print(f"평균 : {sum(value)/len(value)}")

# 몫과 나머지를 구하는 함수
print(divmod(sum(value),4))

# 외장 함수 : 파이썬의 표준 모듈이지만 import해야 사용 가능
import random

for i in range(10):
    #rand = random.randint(0,4) # 0~4 사이의 임의의 정수 반환(4포함)
    rand = random.randrange(0,4)  # 0 ~4 미만
    print(rand)

# 날짜 및 시간 관련 함수
from datetime import datetime # datetime 모듈에서 datetime 함수만 사용하겠다는 뜻
print(datetime.today()) # 현재 날짜 시간 밀리초까지
print(datetime.today().year)  # 현재 년도
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 달력 생성
import calendar
print(calendar.calendar(2024))
print(calendar.calendar(2024, m=5)) # 한 줄에 5개씩
print(calendar.month(2024, 3)) # 특정 달 지정

# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))

print(math.ceil(1.0001))
print(math.floor(1.0001))





