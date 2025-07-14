# numpy 실습4
import numpy as np

# .arange(1,101) : 100개 난수 생성-범위 주의
# .reshape(-1,1) : 1열짜리 배열로 변환
num = np.core.arange(1,101).reshape(-1,1)
# normal(22,5,100) : (평균,표준편차,생성개수)에서 랜던 추출한 배열 생성
age = np.round(np.random.normal(22,5,100), 1).reshape(-1,1)
hei = np.round(np.random.normal(170,10,100), 1).reshape(-1,1)
wei = np.round(np.random.normal(70,10,100), 1).reshape(-1,1)

stu = np.concatenate([num,age,hei,wei], axis=1)
print(stu)

print('\n<평균> 나이/키/몸무게')
# stu[:,1:] : [행,열]. 행은 전부, 열은 1열부터 끝까지
res = np.mean(stu[:,1:], axis=0)
print(res)

print('\n<표준편차> 나이/키/몸무게')
res = np.std(stu[:,1:], axis=0)
print(res)

print('\n<키 190 이상> 번호/나이/키/몸무게')
res = stu[stu[:,2] >= 190]
print(res)

print('\n<몸무게 90 이상> 번호/나이/키/몸무게')
res = stu[stu[:,3] >= 90]
print(res)