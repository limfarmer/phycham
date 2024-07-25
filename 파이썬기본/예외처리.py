# 예외처리 :
# 1. 문법 오류 수정, 논리적인 문제가 없도록 코딩, 항상 예외 사항을 대비하는 코드 작성
# 2. 해결가능 예외 사항이 있고, 해결 불가능한 예외 사항이 있음
try:
    print("나눗셈 계산기")
    num1 = int(int("첫 번쨰 : "))
    num2 = int(int("두 번쨰 : "))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("입력 error!")
except ZeroDivisionError as err:
    print(err)
else:
    print("정상 처리")
finally: print("프로그램 실행 완료!!")