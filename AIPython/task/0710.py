# 실습1-(1)
import numpy as np

arr = np.arange(-5,6)
print(arr, end='\n\n')

arr = np.arange(0, 44.5, 0.5)
print(arr, end='\n\n')

arr = np.linspace(5, 61, 16)
print(arr, end='\n\n')

arr = np.array([range(1,6), range(11,16), range(21,26)])
print(arr, end='\n\n')

print('구조 : ', arr.ndim)
print('차원구조 : ', arr.shape)
print('요소개수 : ', arr.size)

# 1로 채워지는 [3,4]-3행 4열 배열
arr = np.ones((3,4))
print(arr, end='\n\n')

# 0으로 채워지는 1차원(길이 10) 배열
arr = np.zeros(10)
print(arr, end='\n\n')

# 5로 채워지는 [4,5] 배열
arr = np.full([4,5], 5)
print(arr, end='\n\n')

# 0~15까지 순차로 채워지는 1차원 정수 배열 -> .reshape(4,4) : [4,4] 배열로 변환
arr = np.arange(0,16).reshape(4,4)
print(arr, end='\n\n')

# .reshape(-1,4) : 4열만 지정, 행은 자동으로 맡길 때
# .transpose() : 위의 배열을 세로방향으로 변환
arr = np.arange(0,16).reshape(-1,4).transpose()
print(arr, end='\n\n')
# arr = arr.transpose()
# print(arr, end='\n\n')


# 실습1-(2)
arr1 = np.arange(1,21).reshape(4,5)
print(arr1, end='\n\n')

arr2 = arr1[1:4, 1:3]
print(arr2, end='\n\n')

# [:, 1::2] : 1열부터 끝까지 2씩 증가
arr3 = arr1[:, 1::2]
print(arr3, end='\n\n')

arr4 = np.zeros(10)
arr4[3:7] = 100 # 3~6번째 항목만 100으로 바꾸기
print(arr4, end='\n\n')

arr5 = np.ones((5,5))
# ::2 : 처음부터 끝까지 2씩 증가
# 1, 3, 5열 & 1, 3, 5행에 해당하는 항목만 100으로 바꾸기
arr5[::2, ::2] = 100
print(arr5, end='\n\n')

# 100으로 채워지는 [5,5] 배열
arr6 = np.full((5,5), 100)
# [0,4]위치, [2,2]위치, [3,0]위치의 항목만 0으로 바꾸기
arr6[[0, 2, 3], [4, 2, 0]] = 0
print(arr6, end='\n\n')


# 실습2
with open('성적.txt', 'r') as fp :
    for n in range(3) : fp.readline()
    score = fp.read().split(',')

score = [int(n) for n in score]
score = np.array(score)

print('<번호순 출력>')
for n, jumsu in enumerate(score) :
    print(f'({n+1}){jumsu}', end=' ')
print('\n-----------')
print('평균 : ', np.mean(score))

maxsu = np.max(score)
# np.where(score == maxsu) 일 때 출력값 : (array([ 1,  4, 27, 46]),) -> 튜플 형태
# + 1 : 리스트 내 항목에 각 +1. 인덱스 배열 순서 + 1 해야 학생 번호와 같음
maxindex = np.where(score == maxsu)[0] + 1
print(f'최고점수 : {maxsu}점 -> 번호 : {maxindex}')

minsu = np.min(score)
minindex = np.where(score == minsu)[0] + 1
print(f'최저점수 : {minsu}점 -> 번호 : {minindex}')

score = np.sort(score) # 오름차순 정렬
score = score[::-1] # 역순

print('<점수가 높은순 출력>')
for jumsu in score :
    print(jumsu, end=' ')
print('\n-----------')

# cnt90 = score >= 90
# print(cnt90)
# 출력값 ; score >= 90 : T or F 값
# [ True  True  True  True  True  True  True  True  True  True  True False
#  False False False False False False False False False False False False
#  False False False False False False False False False False False False
#  False False False False False False False False False False False False
#  False False]
cnt90 = sum(score>=90) # True(1)인 값만 더함 == 인원수
print(f'90점 이상 인원수 : {cnt90}명')

cnt50 = sum(score<50)
print(f'50점 미만 인원수 : {cnt50}명')
print()

# 실습3
with open('중간고사.txt', 'r', encoding='utf-8') as fp :
    for n in range(2) : fp.readline()
    mid = fp.read().split()

with open('기말고사.txt', 'r', encoding='utf-8') as fp :
    for n in range(2) : fp.readline()
    final = fp.read().split()

mid = [int(n) for n in mid]
mid = np.array(mid).reshape(-1, 4) # 열만 4개로 지정
final = [int(n) for n in final]
final = np.array(final).reshape(-1, 4)

stuno = mid[:,0].reshape(-1, 1) # 학생 번호만 추출
avg = (mid[:,1:] + final[:,1:]) / 2 # 행-처음부터 끝까지, 열-2열(인덱스 1번)부터 끝까지 -> 각각(중간 + 기말) /2
stu_avg = np.round(np.mean(avg, axis=1), 1) # axis=1 : 행(->) 방향으로, np.round(~, 1) : 소숫점 1번째 자리까지 반올림
stu_avg = stu_avg.reshape(-1,1) # 세로로 정렬

allstu = np.concatenate((stuno, avg, stu_avg), axis=1) # 가로 방향으로 합치기(20행짜리 세로방향 배열 여러 개를 합침)

print('-'*50)
print('번호\t 국어\t 수학\t 영어\t 평균')
print('-'*50)
# stu[0]:^4.0f : 학생번호는 정수처럼 출력. ^ : 가운데정렬
for stu in allstu :
    print(f'{stu[0]:^4.0f}\t {stu[1]:.1f}\t {stu[2]:.1f}\t {stu[3]:.1f}\t {stu[4]:.1f}\t')
print('-'*50)
