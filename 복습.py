def while_sum(n):
    sum = 0
    while n:
        sum += n
        n -= 1
    return sum

def recu_sum(a):
    if a == 1: return 1
    else: return a + recu_sum(a-1)

a = int(input("정수를 입력 하세요 : "))
print(recu_sum(a))