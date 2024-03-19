# 회원가입을 위한 아이디/패스워드 입력 확인
# user = input("아이디 입력 : ")
#
# if len(user) >= 8 :
#     pwd = input("비밀번호 입력 : ")
#     if len(pwd) < 8 or len(pwd) > 16 :
#         print("비밀번호는 8자에서 16자 사이여야 합니다.")
#     elif pwd.find(user) >= 0 : # 해당 문자열의 인덱스를 반환, 없으면 -1
#         print("비밀번호에 아이디를 포함 시킬 수 없습니다.")
#     else :
#         print(f"아이디 : {user} \n비밀번호 : {pwd}")
# else :
#     print("아이디는 반드시 8자리 이상이어야 합니다.")

# 1번
#number = int(input("세자리 정수 입력 : "))
# first = int(number / 100)
# second = int((number / 10) % 10)
# third = int(number % 10)

# if first > second and first > second :
#     print(first)
# elif second > third :
#     print(second)
# else: print(third)

# max를 활용한 방법
# number2 = list(map(int,input("세자리 정수 입력 : ")))
# print(max(number2))

# 2번
lunch_or_night = int(input("주간근무 [1], 야간근무[2]를 입력 하세요 : "))
work_time = int(input("근무 시간을 입력해 주세요 : "))

wage = 9860  # 시급

if lunch_or_night == 1 :
    print(f"{work_time}시간 동안 근무한 주간 급여는 {wage * work_time}원 입니다.")
else :
    print(f"{work_time}시간 동안 근무한 야간 급여는 {format(int((wage*1.5) * work_time), ',')}원 입니다.")