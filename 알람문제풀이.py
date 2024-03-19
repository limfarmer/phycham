# H M 주어지고 설정 시간보다 45분 일찍 설정됨

H = int(input("H : "))
M = int(input("M : "))

# 1440분 24시간

trans_to_min = (H * 60) + M  # 입력받은 시간을 분으로 바꾼후 더함
# print(int((sum-45) / 60)) # 시간
# print((sum-45) % 60) # 분

rsH = int((trans_to_min - 45) / 60)  # 총 시간에서 45분을 뺀후 60으로 나눠서 시간값 구함
rsM = (trans_to_min - 45) % 60  # 총시간에서 45분을 뺀후 나머지 연산자로 남은 분값 구함

if 0 <= H <= 24 and 0 <= M <= 59:
    if trans_to_min < 45: # 총 시간 값이 45분 보다 적을 경우 -> 0시 44분 이하여서 23시로 넘어가야 될 경우
        H = 23
        print(f"{H}:{rsM}")
    else:
        print(f"{rsH}:{rsM}")
else:
    print("입력한 시간이 표현 범위를 넘었습니다.")
