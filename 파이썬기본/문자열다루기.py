# 문자열이란 문자로 이루어진 데이터의 집합,
# 파이썬은 문자를 별도로 다루지 않고 전부 문자열로 간주
# " ", ' ', """ """, ''' '''

# 인덱싱 : 시퀀스 자료형(리스트, 튜플, 문자열)에서 특정 위치의 요소를 선택하는 작업
#  ㄴ> seq[index]
# 슬라이싱 : 시퀀스 자료형에서 일부분을 추출
#  ㄴ> seq[start:end:step]
my_list = [0,1,2,3,4,5,6,7,8,9]  # 리스트 생성[]
난널믿었던만큼난내친구도믿었기에 = my_list[2:7] # 인덱스는 0부터 시작,end는 미만
난아무런부담없이널내친구에게소개시켜줬고 = my_list[1:9:2] # 1,3,5,7

# 인덱싱, 슬라이싱 실습
# 주민등록번호 자르기, 하위 7자리중 첫번째 자리는 성별, 앞의 6자리는 년,월,일
그런만남이있은후부터우린자주함께 = "991120-1234567"
print("성별 : " + 그런만남이있은후부터우린자주함께[7])
print("년 :" + 그런만남이있은후부터우린자주함께[:2]) # 0~2 미만
print("월 : " + 그런만남이있은후부터우린자주함께[2:4])
print("일 : " + 그런만남이있은후부터우린자주함께[4:6])
print("생년월일 : " + 그런만남이있은후부터우린자주함께[:6])
print("뒤 7자리 : " + 그런만남이있은후부터우린자주함께[7:])  # 7에서부터 끝까지
print("- 값으로 뒤 7자리 : " + 그런만남이있은후부터우린자주함께[-7:])

python_str = "Life is too short, You need Python"
new_str = python_str[0] + python_str[1] + python_str[2] + python_str[3]
# python_str[0] = "l" # 리터럴 상수이기 때문에 변경 안됨
print(new_str)

# 대소문자 : upper(), lower()
print(python_str.upper())
print(python_str.lower())

# 문자열 변경
a_str = "Hello Python Program"
new_str2 = a_str.replace("Pyhhon","Java")
print(new_str2)

# 문자열에 포함된 문자 갯수 세기(count()), 문자열 길이(len(), __len__)
print(a_str.count('l')) # 해당 문자열에서 count()함수에 전달된 문자가 몇개 존재하는지 반환
print(len(a_str)) # 문자열 길이를 반환하는 함수
print(a_str.__len__()) # 문자열 길이를 반환하는 내장 함수

# 문자열 찾기
# find() : 찾은 문자열 인덱스 반환, 없으면 -1
# rfind() : 뒤에서 부터 문자열을 찾고 찾은 인덱스는 앞에서 계산
# index() : 찾은 문자열의 인덱스 반환, 없으면 ValueError

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"), " d")
print(phrase.index("포기"))
print(phrase.find("나에게"))
# print(phrase.index("나에게")) 에러 발생
new_str = phrase.replace("가장","나에게")
print(new_str)

# 문자열 연산자 : "" + "", "" * 3
print("태양고" + "나희도")
print("태양고" * 2)
# print("태양고" + 2) 이건 안됨

# 문자열 양옆 공백 제거 : strip()
input_a = """
    안녕하세요.
   문자열 함수를 알아 봅니다.

a"""
print(input_a.strip())





