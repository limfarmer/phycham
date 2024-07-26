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

# 배열의 연산 : 배열의 다향한 연산을 할 수 있음 단, 배열의 형태가 같아야함
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

# 요소별 비교 연산
arr3 = np.array([10,20,30,40,50])
print(arr3 > 20)

# 통계를 위한 연산 : 배열의 힙, 표준 편차, 분산, 최대값과 최소값, 누적합, 누적곱 등
# 통계에서 많이 사용하는 메소드를 제공해줌
arr4 = np.arange(5) # 0 ~ 5 미만의 값 생성
print(arr4)
print(f"합계 : {arr4.sum()}")
print(f"평균 : {arr4.mean()}")
print(f"표준 편차 : {arr4.std()}")
print(f"분산 : {arr4.var()}")
print(f"최소값 : {arr4.min()}")
print(f"최대값 : {arr4.max()}")

# 배열의 인덱싱 / 슬라이싱 
arr5 = np.array([1,2,3,4,5])
#인덱싱
print(arr5[3]) # 네번째 요소
# 슬라이싱
print(arr5[:4]) # 0번째 인덱스부터 4번 인덱스 미만까지 값을 잘라냄

# Universal 함수 : 배열의 원소별 연산을 지원하는 함수
arr6 = np.array([1,2,3,4,5])
arr7 = np.arange(6,11)
print(arr6)
print(arr7)
print(f"add : {np.add(arr6, arr7)}")
print(f"sub : {np.subtract(arr6, arr7)}")
print(f"mul : {np.multiply(arr6, arr7)}")
print(f"div : {np.divide(arr7, arr6)}")
print(f"pow : {np.power(arr6, arr7)}") # 제곱

# 행렬 연산 : 행렬간의 연산, 다차원 배열
matrix1= np.array([[1,2],[3,4]])
matrix2= np.array([[5,6],[7,8]])

# 행렬 덧셈
print("------ 다차원 행렬 산수 ---------")
print(np.add(matrix1,matrix2))
print(np.subtract(matrix1,matrix2))
print(np.multiply(matrix1,matrix2))

# 전치 행렬 : 행과 열을 교환하여 얻어진 행렬
matrix3 = np.array([[1,2],[3,4]])
result = np.transpose(matrix3)
print(result)

# 역 행렬
matrix4 = np.array([[1,2],[3,4]])
inverse_matrix = np.linalg.inv(matrix4)
print(inverse_matrix)

# 정렬과 탐색
x_sort = np.array([9,8,7,12,13,2,1,5])
print(np.amin(x_sort))
print(np.amax(x_sort))
print(np.argmin(x_sort)) # 최소값이 있는 위치
print(np.argmax(x_sort)) # 최대값이 있는 위치
print(np.sort(x_sort)) # 오름차순 정렬
print(np.argsort(x_sort)) # 값의 인덱스

# 브로드 캐스트 : 배열 크기가 다를 경우에도 연산 지원
print("=" * 7, "브로드 캐스팅 연산", "="*7)
aa = np.array([1,2,3]) # 1행 3열
bb = np.array([[4],[5],[6]]) # 3행 1열

cc = aa + bb
print(cc)
