import pandas as pd

# 실습1
score = pd.read_csv('성적.csv', encoding='cp949')
print(score.head()) # 처음 5줄만 추출
print(score.tail()) # 마지막 5줄
print(score.info()) # 자료형
print(score.iloc[:,3:5].describe()) # 통계정보 확인

# 1-(2) 항목 추가
score.loc[100] = ['디자인학과', 300022, '김철수', 90, 90, 10]

# 1-(3) '과제' 열 삭제. axis=1 : 열 방향으로 지정
score2 = score.drop('과제', axis=1) 
score.drop('과제', axis=1, inplace=True) # 원본 파일을 수정

# 1-(4) '출석' 열 전체항목 20으로 추가
score['출석'] = 20 # '출석' 열이 기존에 존재하지 않을 때

# 1-(5) '김민진' 학생 정보 삭제. axis 지정 X -> 기본은 행 방향
# 김민진 인덱스 값 = 2였음
score.drop(2, inplace=True)

# 1-(6) 평균, 결과 추가
# score.중간 * 0.4 : 100개의 '중간' 배열에 모두 0.4씩 곱해짐
score['평균'] = score.중간 * 0.4 + score.기말 * 0.4 + score.출석
# 평균이 80 이상이면 ‘PASS’ 60 이상이면 ‘재시험’ 60 미만은 ‘FAIL’
score['결과'] = 'FAIL'
score.loc[score.평균 >= 60, '결과'] = '재시험'
score.loc[score.평균 >= 80, '결과'] = 'PASS'

# 1-(7)
# 내림차순 정렬-평균 기준. ascending=True가 기본값-오름차순 정렬
score = score.sort_values('평균', ascending=False)
# csv 파일로 저장. index=False : index 제외
score.to_csv('성적처리결과표.csv', index=False, encoding='cp949')


# 실습2
tt = pd.read_csv('타이타닉.csv', encoding='cp949')
# 2-(1) 결측지 있는 컬럼 확인
print(tt.isna().sum()) # NaN 값이 있는지 열별로 확인

# 2-(2)
print('전체 인원수 : ', tt.이름.count()) # 총 항목 개수 확인

# 2-(3)
print('나이 미상 인원수 : ', tt.나이.isna().sum())

# 2-(4) 나이 미상인 데이터 삭제-기본 옵션 any(하나라도 NaN이면 행 삭제)
tt2 = tt.dropna()
print('나이 미상 삭제 후, 전체 인원수 : ', tt2.이름.count())

# 2-(5) 최고/최저 나이 승객 출력
print('\n<최고 나이/최저 나이 명단>')
# | : or
res = tt2[(tt2.나이 == tt2.나이.max()) | (tt2.나이 == tt2.나이.min())]
# 이름, 성별, 나이만 출력
print(res[['이름', '성별', '나이']])


# 실습3
job1 = pd.read_csv('취업정보1.csv', encoding='cp949')
job2 = pd.read_csv('취업정보2.csv', encoding='cp949')
job3 = pd.read_csv('취업정보3.csv', encoding='cp949')

# 3-(1) 파일 3개 합치기. 기존 인덱스는 무시
job = pd.concat([job1, job2, job3], ignore_index=True)

# 마감일 내용 자료형이 현재 object(문자열) -> datetime 자료형으로 변환
job['마감일'] = pd.to_datetime(job.마감일)

# 마감일 중 월(month)만 추출
job['마감_월'] = job.마감일.dt.month 

# 마감일 중 일(day)만 문자로 추출
job['마감_요일'] = job.마감일.dt.day_name() 

# 3-(2) 조회수 상위 10개
print('\n<조회수 상위 10개>')
res = job.sort_values('조회', ascending=False) # 조회수 기준 내림차순 정렬
print(res.head(10)) # 처음 10개 출력
print(res.iloc[:, 0:7].head(10)) # 처음~6열까지만 출력_마감월, 요일 제외

# 3-(3) 조회수 하위 10개
print('\n<조회수 하위 10개>')
res = job.sort_values('조회') # 조회수 기준 오름차순 정렬
print(res.iloc[:, 0:7].head(10))

# print('\n<조회수 하위 10개>')
# res = job.sort_values('조회', ascending=False) # 조회수 기준 내림차순 정렬
# print(res.iloc[:, 0:7].tail(10))

# 3-(4) 마감일 8월인 정규직 정보만 출력
print('\n<마감일이 8월, 정규직>')
res = job[(job.마감_월 == 8) & (job.채용형태 == '정규직')]
# 회사명, 채용형태, 마감일만 출력
print(res[['회사명', '채용형태', '마감일']])

# 3-(5)
print('\n<채용형태별 조회수 평균>')
# .groupby('채용형태') : 채용형태 열을 같은 내용끼리 묶음(그룹화)
# ['조회'].mean() : 조회수의 평균 구하기
res = job.groupby('채용형태')['조회'].mean()
print(res)

# 3-(6)
print('\n<마감 요일별 개수>')
# .groupby('마감_요일') : 마감_요일 같은 내용끼리 묶음
# ['회사명'].count() : 각 요일별 개수 세기-아무 항목이나 기준으로 가능
res = job.groupby('마감_요일')['회사명'].count()
print(res)
print('\n내림차순으로 정렬')
res = res.sort_values(ascending=False)
print(res)

# .value_counts() : 요일별 그룹화 + 기본으로 내림차순으로 정렬해줌
print('\n2번째 방법')
res = job.마감_요일.value_counts()
print(res)