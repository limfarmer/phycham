import numpy as np
# 배열이란? 순서가 있는 같은 종류의 데이터가 저장된 집합을 의미

data = [1,2,3,4,5,6,7] # 리스트 생성
a1 = np.array(data) # 리스트를 넘파이 배열로 변환

data2 = [0,1,3,4,0.5,3.14,9.99] # 리스트는 데이터형에 제한을 받지 않음
a2 = np.array(data2) # 그러나 넘파이 배열은 데이터형에 제한을 받기 때문에 다른 타입을 자동 형변환함

#print(a2) # 전부 double타입으로 변환됨

x = np.array([0.1,0.2,0.3])
#print(x)
#print(x.shape) # 배열의 형태를 나타냄
#print(x.dtype) # 배열 요소의 데이터 타입을 반환

y = np.array(([1,2,3],[4,5,6]))
#print(y)
#print(y.shape) # (2,3)이라고 찍히는데 2행 3열이라는뜻
#print(y.dtype)

# 범위를 지정해 배열 생성 arange()
a3 = np.arange(0,10,0.5) # 0 ~ 10 미만, 2씩 증가, 생략시 1씩
#print(a3)

# 배열의 형태 변경
a4 = np.arange(12).reshape(4,3) # 0 ~ 12 미만의 배열을 생성하고 배열의 구조를 3행 4열로 만드는것
#print(a4)
#print(a4.shape)

# 범위의 시작과 끝을 지정하고 갯수를 지정
a5 = np.linspace(1,10,20)
print(a5)
# 0 ~ 파이값까지 동일한 간격으로 20개 데이터 생성
a6 = np.linspace(0, np.pi, 20)
print(a6)

# 특별한 형태의 배열 생성
a7 = np.zeros(10) # 0으로 초기화된 10개의 배열 생성
print(a7)

a8 = np.zeros((3,4)) # 0으로 초기화된 2차원(3*4)배열 생성
print(a8)

a9 = np.ones(10)
print(a9)

a10 = np.ones((3,4))
print(a10)

# 단위 행렬 만들기 : n * n인 정사각형의 행렬의 주대각선이 모두 1이고 나머지는 0인 행렬
a11 = np.eye(4)
print(a11)

# 배열의 데이터 타입 변환
a12 = np.array(['1.5','0.62','2','3.14','3.141592'])

print(a12)
print(a12.dtype)

num_a12 = a12.astype(float)
print(num_a12)

a13 = np.array(['1', '3', '5', '7', '9'])
num_a13 = a13.astype(int) # 문자열을 정수 타입으로 변환
print(num_a13)

#난수 배열 생성
a14 = np.random.rand(2,3) # 0 ~ 1 미만의 난수 생성, 2행 3열
print(a14)
print("------------")
a15 = np.random.rand(2,3,4) # 2면 3행 4열
print(a15)

# 지정한 범위에 해당하는 정수로 난수 배열을 생성
a16 = np.random.randint(10,size=(3,4))
print(a16)