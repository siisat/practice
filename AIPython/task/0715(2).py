import pandas as pd

# 0714 실습3 -> 차트 그리기

job1 = pd.read_csv('취업정보1.csv', encoding='cp949')
job2 = pd.read_csv('취업정보2.csv', encoding='cp949')
job3 = pd.read_csv('취업정보3.csv', encoding='cp949')
job = pd.concat([job1, job2, job3], ignore_index=True)
job['마감일'] = pd.to_datetime(job.마감일)
job['마감_월'] = job.마감일.dt.month 
job['마감_요일'] = job.마감일.dt.day_name()



####
# 요일을 숫자로 변환해서 새 배열 생성
# weekday() 하면 오류남
job['요일번호'] = job.마감일.dt.weekday
# print(job.head())





# print('\n<조회수 상위 10개>')
# res = job.sort_values('조회', ascending=False) # 조회수 기준 내림차순 정렬
# print(res.head(10)) # 처음 10개 출력
# print(res.iloc[:, 0:7].head(10)) # 처음~6열까지만 출력_마감월, 요일 제외

# print('\n<조회수 하위 10개>')
# res = job.sort_values('조회') # 조회수 기준 오름차순 정렬
# print(res.iloc[:, 0:7].head(10))

# print('\n<마감일이 8월, 정규직>')
# res = job[(job.마감_월 == 8) & (job.채용형태 == '정규직')]
# print(res[['회사명', '채용형태', '마감일']])
# res = job.groupby('채용형태')['조회'].mean()
# print(res)





####

print('\n<마감 요일별 개수>')
res = job.groupby('요일번호')['회사명'].count()
print(res)


import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

x = res.index
y = res.values

x_name = ['월','화','수','목','금','토','일']
plt.bar(x,y)
plt.xticks(x, x_name)
plt.ylim(0,25)

for n in range(7) :
    plt.text(n, y[n]+0.2, str(y[n])+'개', c='red', ha='center')

plt.show()