# while문 : 참인 동안 반복 수행, 반복 횟수를 알 수 없을때 주로 사용
# 입력 받은 정수의 합 구하기
# n = int(input("정수 입력 : "))
# sum = 0
#
# while n:
#     sum += n
#     n -= 1
# print(sum)

while True:
    age = int(input("나이를 입력 : "))
    if 0 <= age < 200: break
    print("난 이제 지쳤어요 땡벌땡벌")

