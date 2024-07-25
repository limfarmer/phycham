# 파이썬 변수 선언 시 데이터 타입을 지정하지 않으며,
# 변수에 값이 대입 될때 형이 결정됨
number = 200
number2 = 3.14
str2 = ""
bool2 = True
print(type(number))  # type() : 변수의 데이터형을 확인
print(type(str2))  # str 타입
print(type(bool2))  # bool 타입
print(type(number2))  # float 타입

# 형변환 : 선언된 변수에 값이 할당되는 순간 형이 결정, 이 후 다른 데이터형으로 변경할때 사용
print(10 + int("20"))
print("나이 : " + str(30))
print(0.1 * float("512.34"))

var = ""  # 공백은 false로 반환
number3 = 0  # 0은 false
number4 = None  # false
print(bool(number3)) # bool 값의 거짓 : "", 0, False, None

