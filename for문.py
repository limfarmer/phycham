# for문은 정해진 범위 만큼 반복 할 때 주로 사용
# for 요소 in 시퀀스: 시퀀스는 리스트, 튜플, 문자열 등을 의미
# fruits = ["사과", "바나나", "자두", "딸기", "수박", "복숭아"]
# for e in fruits:
#     print(e, end=",")
# print()

# for 변수 in range(시작값, 종료값, 증감값): 자바의 일반적인 for문과 유사
# n = int(input("정수 : "))
# sum2 = 0
# for i in range(1, n+1): # 1부터 n까지 -> 종료값(n)은 미만 개념이라 +1해줘야 n값일때 종료, 증감값은 생략하면 1씩 증가
#      sum2 += i
# print(sum2)

# 이중 for문
# n = int(input("정수 : "))
# for i in range(n):
#     # n -= 1
#     for j in range(n):
#         print("*", end=" ")
#     print()

# 구구단 출력
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i * j}")
#     print("-" * 10)
#
# # 이중 for문과 조건문 사용
# n = int(input("정수를 입력 하세요 : "))
# for i in range(n):
#     for j in range(n):
#         if j % 2 == 0:  # 짝수
#             print("#", end=" ")
#         else:
#             print("*", end=" ")

# 별찍기, 사각형 찍기 11:10분까지
#star = int(input("정수 입력 : "))
# for i in range(1,star+1):
#     for j in range(1,star+1):
#         print("*", end="")
#     print()

# for i in range(1, star * star +1):
#     print(f"{i:3}",end="")
#     if i % star == 0: print() # 입력 받은 수의 배수 마다 줄 바꿈
#
# for i in range(star):
#     for i in range(star-i):
#         print("*", end="")
#     print()
#
# for i in range(0, star+1):
#     for j in range(i):
#         print(" ", end="")
#     for l in range(star-i):
#         print("*", end="") # 감소 x
#     print()

# for문에서 continue 사용
# n = int(input("정수 : "))
# for i in range(n):
#     if i % 2 != 0 : continue
#     print(i, end=" ")

# for문을 반대로 반복하기
for i in range(10, 0 - 1, -1):
    print(f"index : {i}")