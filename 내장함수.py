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
