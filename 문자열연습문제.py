# 1번 3개의 정수를 입력받아 최대/소값 구하기
import datetime

# 2번 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기


# 1번
# number = list(map(int,input("정수 입력 :").split()))
# if number[0] > number[1] & number[0] > number[2] :
#     print(number[0])
# elif number[1] > number[2]:
#     print(number[1])
# else :
#     print(number[2])

# 2번 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
# 2번 940502 1111111
# ID_num = input("주민번호 입력(- 없이) : ")
# mil = ID_num[:1]
# birth = ID_num[:6]
# gender = int(ID_num[6:7])
#
# year = datetime.datetime.now().year
#
# age = ((year % 100) + 100 - int(ID_num[:2])) + 1
#
#
# if gender == 1 or gender == 3 :
#     print(f"생년월일 : {birth} \n성별 : 남 \n나이 : {age}\n")
# elif gender == 2 or gender == 4 :
#     print(f"생년월일 : {birth} \n성별 : 여 \n나이 : {age}\n")
# else: pass

# 3번 2개의 문자열 변수 S와 K에, 양의 정수를 변수 n에 각각 전달 받아
# S 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
# 예) s : seoul
# k : korea
# n : 2
# result : ulkorea

# n = int(input("n : "))
# s = input("s : ")
# k = input("k : ")
#
# print(s[-n:] + k)
# print(s[len(s)-n:] + k) 앞에서부터 계산

# 여러개의 정수를 입력받아 합계와 편균 구하기
num2 = list(map(int,input("정수 여러개 입력 : ").split()))
print(f"합계 : {sum(num2)}")
print(f"평균 : {sum(num2)/len(num2)}")