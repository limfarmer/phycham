# 문자열을 입력 받아 대문자는 소문자로, 소문자는 대문자로 변경
# rst =""
# for e in input("단어 입력 : "):
#     if e.islower():
#         rst += e.upper()
#     else:
#         rst += e.lower()
# print(rst)

A = int(input())
B = int(input())
C = int(input())
rs = str(A * B * C)


for i in range(10):
    print(rs.count(str(i)))
