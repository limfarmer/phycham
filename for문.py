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
# star = int(input("정수 입력 : "))
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

# for문을 반대로 반복 하기
# for i in range(10, 0 - 1, -1):
#     print(f"index : {i}")

# for문으로 알파벳 출력
# chr(유니코드 값을 입력 받아 문자 출력)
# ord(문자의 유니 코드 값을 반환)

# for i in range(ord("A"), ord("Z") + 1 ):
#     print(chr(i), end=" ")
# print()
#
# for i in range(65, 91): # A : 65, Z : 90
#     print(chr(i), end=" ")

# 회원정보 출력하기


# name = input("이름 입력 : ")
# age = int(input("나이 : "))
# if 0 > age > 200: age = input("범위 넘음 재입력 : ")
# gender = input("성별 : ")
# if gender != "M" and "m" and "F" and "f" and "남성" and "여성":
#     gender = input("잘못된 성별 입력 재입력 : ")
# jobs = int(input("직업 : "))
# if jobs == 1:
#     job = "학생"
# elif jobs == 2:
#     job = "회사원"
# elif jobs == 3:
#     job = "주부"
# elif jobs == 4:
#     job = "무직"
# else:
#     jobs = int(input("잘못된 직업 입력 재입력 : "))
#
# print(f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {job} ")

# 회원 정보 정답
# 함수 만들어서 풀기
def input_age():
    while True:
        age = input("나이를 입력 : ")
        if age.isdigit():  # 문자열이 숫자로 구성되어 있는지 확인
            age = int(age)
            if 0 < age < 200:
                return age
        print("나이를 잘못 입력")

def input_gender():
    while True:
        gender = input("성별 입력 : ")
        if gender == "M" or gender == "m": return "남성"
        elif gender == "F" or gender == "f": return "여성"
        print("성별을 잘못 입력 했습니다.")

def input_jobs():
    while True:
        jobs = input("직업을 입력 : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업을 잘못 입력 했습니다.")

# [] 리스트, {} 딕셔너리, () 튜플
def print_info(name,age,gender,jobs):
    jobs_str = "", "학생", "회사원", "주부", "무직" # 튜플
    print("="*3, "회원정보", "="*3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"

# 함수 호출과 파일 저장하기
fd = open("member.txt", "wt", encoding="utf-8")
while True:
    name = input("이름 입력 / 종료는 exit :")
    if name == "exit": break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name,age,gender,jobs)
    fd.write(rst + "\n")
fd.close()


