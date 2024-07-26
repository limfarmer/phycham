import numpy as np
import pandas as pd

# 1차원 배열 (시퀀스)
s1 = pd.Series([10,20,30,40,50]) # 리스트 구조로 데이터를 입력
#print(s1) # 출력 결과에 인덱스가 포함되어서 출력됨

s2 = pd.Series(['a','b','c',1,2,3])
#print(s2) # object타입 반환

# 데이터가 없는 경우에 대한 처리
s3 = pd.Series([np.nan,10,20,30])
#print(s3)

#인덱스 추가하기
index_date = ['2024-07-26','2024-07-27','2024-07-28']
s4 = pd.Series()

# 날짜 자동 생성
s6 = pd.date_range(start='2024-07-20',end='2024-07-28')
#print(s6)

# 달력을 요일을 기준으로 일주일씩 증가
s7 = pd.date_range(start='2024-07-20',periods=4, freq='W')
# print(s7)

# 데이터 프레임 행과 열로 구성된 사각형 모양의 표
df = pd.DataFrame({'name' : ['민지', '하니', '혜린', '다니엘', '혜인'],
                   'kor' : [90, 88, 97, 77, 92],
                   'eng' : [88, 92, 87, 96, 96]})

# print(df)
# print(sum(df['eng']))
# print(sum(df['eng'])/df['eng'].size)

df2 = pd.DataFrame({
    'goods' : ['apple','strawberry','watermelon'],
    'price' : [1800 , 1500, 3000],
    'salesRate' : [24,38,13]
})
# print(df2)
# print(sum(df2['price'])/df2['price'].size)
# print(sum(df2['salesRate'])/df2['salesRate'].size)


df_exam = pd.read_excel('excel_exam.xlsx')
#print(df_exam)

df_csv = pd.read_csv('exam.csv')
print(df_csv)
