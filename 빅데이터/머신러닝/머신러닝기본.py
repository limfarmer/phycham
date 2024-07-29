# 도미의 길이
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
# 도미의 무게
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# 빙어의 길이
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
# 빙어의 무게
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import matplotlib.pyplot as plt
plt.scatter(bream_length,bream_weight)
plt.xlabel('length')
plt.ylabel('weight')
#plt.show()

plt.scatter(smelt_length,smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
#plt.show()

# 첫 번째 머신러닝 : k-최근접 이웃
# 하나의 데이터로 합치기
length = bream_length + smelt_length
weight = bream_weight + smelt_weight

# 2차원 리스트 만듵기 , zip함수는 나열된 리스트 각각에서 하나의 원소를 꺼내서 반환
fish_data = [[l,w] for l,w in zip(length,weight)]
#print(fish_data)

fish_target = [1] * 35 + [0] * 14
#print(fish_target)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier() # 객체 생성

# 훈련시키기
kn.fit(fish_data,fish_target)

# 새로운 데이터 입력에 대한 예측
kn.predict([[30,600]])
# print(kn._fit_X)
# print(kn._y)

kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(fish_data, fish_target)
kn49.score(fish_data,fish_target)
print(35/49)




