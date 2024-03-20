# 리스트란 연속적으로 저장되는 형태의 자료형, 크기가 동적으로 변함
# 자바와 다른점은 여러가지 데이터 타입이 섞여 있을 수 있음
# 리스트내에 리스트가 존재할수 있음
# 리스트는 읽기/쓰기 가능, 튜플은 동일한 구조이지만 읽기만 가능

# number = [1,2,3,4,5,6,7,]
# fruits = ['apple','banana','orange']
# mixed = [1,'apple',True,3.14,fruits]
#
# print(number[1])
# print(mixed[4][0][1]) # 배열안에 배열의 1번째 인덱스의 글자
# print(fruits[1][2])
# print(mixed[2])
# print(len(mixed[4]))
# print(mixed[4][2][5])
# print(mixed[4][2][-5]) # 뒤에서 부터 인덱스 세기
#
# list_a = [1,2,3]
# list_b = [4,5,6]
# list_c = list_a + list_b
# print(list_c)
#
# new_list = [1,2,3]
# new_list.append(4)  # 뒤에 값을 추가
# new_list.append(5)
# new_list.append(6)
# new_list.insert(1,1000)  # 1번 인덱스 자리에 1000을 추가
# print(new_list)
# 리스트에서 값 제거하기 : pop, remove, clear
# pop : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제

# print(new_list.pop(1)) # 인덱스 1인 1000 제거후 반환
# new_list.remove(3) # 해당 값을 제거, 동일한 값이 여러개 존재하는 경우 낮은 인덱스값 제거
# print(new_list)
#new_list.clear()  # 전체 삭제하지만 빈 리스트는 남아있음
# del new_list[3]  # 3번 인덱스 삭제
# print(new_list)


# 변수와 리스트의 차이 비교
# kor, eng, mat = map(int,input().split())
# total = kor + eng + mat
# print(total/3)
#
# score = list(map(int,input().split()))
# print(sum(score)/len(score))

# 중복 제거
my_list = ['a','p','p','l','e','a','A']
new_list =[]
for e in my_list:
    if e not in new_list:
        new_list += e # new_list.append(e)도 가능
print(new_list)

# 리스트 순회하기
for e in my_list:
    print(e, end=" ")

# 리스트 순회 전통적인 방법
print()
for i in range(len(my_list)):
    print(my_list[i], end=" ")

# 1 ~ 45까지의 로또 번호 6개를 자동 생성하기


