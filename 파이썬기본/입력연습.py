# 사용자의 입력을 처리하는 input() 함수, 기본값은 문자열로 입력됨
# name = input("이름을 입력하세요 : ")
# print(name)
# kor = int(input("국어 성적을 입력하세요 : "))
# print(f"국어 : {kor}")

# spilt 기본 공백기준으로 나눔
# map : 입력한 갯수만큼 반환함, 가공된 결과값을 반환
# map(변환할 변수 타입이나 함수(콜백 함수)자리 , 들어올 인자 값 자리(입력되는 데이터)
# map 의 특징은 입력 받은 데이터를 동일한 갯수만큼 변환해서 반환
# kor, eng, math = map(int,input("국어 영어 수학 : ").split())
# print(f"국어 : {kor}, 영어 : {eng}, 수학 : {math}")
#
# name, addr =input("이름과 주소 입력 : ").split()
# print(f"이름 : {name}, 주소 : {addr}" )

# 입력의 제한없이 다 받고 싶은 경우
score = list(map(int,input("성적을 마음대로 입력 : ").split()))
print(f"성적을 리스트 출력 : {score}")

# split 활용
# hour, min, sec = input("시:분:초 ").split(":")
# print(f"{hour}시 {min}분 {sec}초")

hour, min, sec = map(int, input("시:뿐:초 ").split(":"))
if(hour > 12) :
    hour -= 12
    print(f"오후{hour:02}시{min:02}분{sec:02}초")
else :
    print(f"오전{hour:02}시{min:02}분{sec:02}초")