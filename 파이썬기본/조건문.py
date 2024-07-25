# 조건문과 반복문은 제어문이라고하고, 이는 순차적인 흐름을 제어하는 목적으로 사용
# 파이썬의 조건문은 자바의 if문과 switch문을 결합한 형태와 유사하며, 파이썬은 switch문 없음
# 조건문의 수행은 들여쓰기로 구분하고 각각의 조건은 :(콜론)으로 구분
# num =int(input("정수 입력 : "))
#
# if num > 100 :
#     print("입력 값이 100보다 커요.")
# elif num < 100:
#     print("입력 값이 100보다 작아요.")
# else:
#     print("입력 값이 100과 같아요")

# season = input("지금 계절 : ")
# if season == "spring" :
#     print("봄이옴")
# elif season == "summer" :
#     print("여름 더움")
# elif season == "fall" or season == "autumn" :
#     print("천고마비의 가을")
# else: print("뻐킹겨울 입니다.")

# 성적에 대한 학점 출력 하기
# 국어, 영어, 수학 성적을 입력 받아 평귤을 구해 등급 출력하기
# 평균 90이상 A, 80이상 B, 70이상 C, 60이상 D, 나머지 F

score = list(map(int, input("점수 입력 : ").split()))
avg = float(sum(score) / len(score))
print(f"{avg:.2f}")
if avg >= 90:
    print('A')
elif avg >= 80:
    print('B')
elif avg >= 70:
    print('C')
elif avg >= 60:
    print('D')
else:
    print('F')

