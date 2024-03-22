# 모듈 : 파이썬 코드를 포함하는 파일(.py)
# 모듈에는 함수, 클래스, 변수 등을 포함할 수 있으며,
# 이러한 요소들은 다른 파이썬 파일에서 improt해서 사용할 수 있음

# 패키지 : 모듈의 집합, 즉 여러개의 모듈을 포함하는 디렉토리
# import math
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))

# math에서 sin,cos만 import(math. 이라는 패키지이름 생략가능)
# from math import sin,cos
# print(sin(1))
# print(cos(1))
# print(tan(1)) tan은 가지고 오지 않았기 때문에 실행 불가

import math as m


# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))
# print(m.floor(2.5))
# print(m.ceil(2.5))

# 해당 패키지인 '모듈과 패키지'만 실행했을 경우
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
    return password


if __name__ == "__main__":
    print(add(10, 40))
    print(sub(4, 2))
