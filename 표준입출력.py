print(38)
print("문자열")
print([1,2,3])
print("파""이""썬")
print("파"+"이"+"썬")
print("파","이","썬") # , 는 파이썬에선 구분자, 기본값은 공백 한칸
print('파''이''썬')
print("\n\n\n") #\n 줄바꿈
print("""
이 사이는 
여러줄로도
 작성 가능
   줄도 상관 없음
공백 들여쓰기도 출력됨
""")

print("안녕하세요. 라고 \"임정후\"가 말했습니다.") # 문자열 내에서 "" 사용
print('안녕하세요. 라고 "임정후"가 말했습니다.') # 이 경우도 사용 가능

print("서울시\t강남구\t역삼동") # \t 탭만큼 간격 띄우기

print("자두\r복숭아") # \r 커서를 앞으로 돌림

# end : 출력 할때 가장 마지막에 자동으로 삽입되는 문자 지정 옵션 ( 기본이 줄바꿈)
# sep : 중간에 삽입되는 문자를 지정하는 옵션 (기본은 공백 한칸)
print("Hello", end="*")
print("Hello World")
# , -> Seperator(구분자)라고 함 기본값 공백
print(1,2,3,4,5,6,7,8,9,10,sep="*")
print("010","1234","4567",sep="-")
year = 2024
month = 3
day = 19
print(year,month,day,sep="/")
