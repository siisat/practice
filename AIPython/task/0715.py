import matplotlib.pyplot as plt

# # 실습1
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# x = range(7)
# month = [10,11,12,1,2,3,4] # month를 바로 사용하면 x축에서 월이 자동으로 정렬됨. 1->12
# cal = [1950, 2350, 1850, 2200, 3800, 2800, 2000]

# plt.figure(figsize=(10,5))
# # 'b-o' : 선 지정자; 파랑 실선 원모양
# plt.plot(x, cal, '-o', label='길동 칼로리')
# plt.legend(loc='upper left') # 범례 표시-label(^ 이거) 지정 후 사용. loc='upper left' : 왼쪽 위에 표시
# # .xticks(x, month) : x축 눈금 변경; x -> month 값으로
# plt.xticks(x, month)
# # ylim(최소,최대) : y축 눈금 변경
# plt.ylim(1500,4200)
# plt.xlabel('월')
# plt.ylabel('칼로리')
# plt.title('<월별 칼로리 분석>')
# plt.grid() # 가로세로선 표시

# # 그래프 위에 숫자로 값 표시
# # n : x축상 위치
# # cal[n]+50 : y축상 위치, cal[n] 값보다 50만큼 위에
# # cal[n] : 이 값을 표시
# # c='red', ha='center' : 색상, 가운데정렬
# for n in range(7) :
#     plt.text(n, cal[n]+50, cal[n], c='red', ha='center')

# plt.show()


# # 실습2
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# x = range(7)
# month = [10,11,12,1,2,3,4]
# cal = [1950, 2350, 1850, 2200, 3800, 2800, 2000]

# plt.figure(figsize=(10,5))

# # 그래프 색상 따로 지정하기-색상 리스트 만들어서 color=리스트명 으로 지정
# col_list = ['skyblue', 'skyblue', 'blue', 'skyblue', 'blue', 'skyblue', 'skyblue',]
# # 막대그래프
# plt.bar(x, cal, width=1, edgecolor='black', color=col_list, label='길동 칼로리')

# plt.legend(loc='upper left') 
# plt.xticks(x, month)
# plt.ylim(1500,4200)
# plt.xlabel('월')
# plt.ylabel('칼로리')
# plt.title('<월별 칼로리 분석>')
# plt.grid()

# for n in range(7) :
#     plt.text(n, cal[n]+50, cal[n], c='red', ha='center')

# plt.show()


# # 실습3
# import numpy as np

# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

# name = ['김철수','박민','강하나','홍길동','김수경','최훈','박하나','강철민','이경민','박경희']
# # numpy 배열로 만들어서 연산
# hei = np.array([156,168,175,160,165,153,190,148,170,159])
# wei = (hei-100)*0.9

# plt.figure(figsize=(10,5))
# plt.bar(name,hei, label='키') # 키 수치가 정상체중 수치보다 더 커서 먼저 그려야 예시처럼 나옴
# plt.bar(name,wei, label='정상체중')
# plt.ylim(0,230)
# plt.legend() # 범례 표시
# plt.xlabel('이름')
# plt.ylabel('키/정상체중')
# plt.title('<키/정상체중 그래프>')

# # 숫자로 값 표시
# for n in range(10) :
#     plt.text(name[n], hei[n]+3, hei[n], ha='center')
#     plt.text(name[n], wei[n]-7, wei[n], ha='center')

# plt.show()


# # 실습4
# import pandas as pd

# plt.rcParams['font.family'] = 'AppleGothic' # 맥 지원 한글 폰트
# plt.rcParams['axes.unicode_minus'] = False

# phy = pd.read_csv('학생체격.csv', encoding='cp949')
# phy['정상체중'] = (phy.키 - 100) * 0.9 # 정상체중 열을 추가함

# # 선 그래프로 바로 그리기 -> 세세한 조정은 X
# # phy.iloc[:, 1:].plot()

# # 각각 열의 값들을 새로운 배열로 추출
# hei = phy.키.values
# wei = phy.체중.values
# n_wei = phy.정상체중.values

# # 정상체중과 10kg 이상 차이 -> 검정, 아니면 회색으로 표시
# cor_list = ['black' if abs(wei[n]-n_wei[n]) >= 10 else 'grey' for n in range(len(hei))]

# # 검정색 개수 표시하는 문장 출력
# blackcnt = cor_list.count('black')
# cnt_print = f'black 색상의 개수 : {blackcnt}개'

# # 키, 체중이 x, y축인 산점도그래프
# plt.scatter(hei, wei, c=cor_list, label='실제체중')

# # 키, 정상체중이 x, y축인 직선그래프
# plt.plot(hei, n_wei, c='red', label='정상체중')

# plt.xlabel('키')
# plt.ylabel('체중')
# plt.title('<전체 학생들의 체중 분포>')
# plt.grid()
# plt.legend()
# # (175, 35, cnt_print, c='red') : x,y축 좌표, 출력할 값, 색상
# plt.text(175, 35, cnt_print, c='red')

# # .show() 한 번만 해야 두 그래프가 한 곳에 그려짐
# plt.show()


# 실습5
import numpy as np
plt.rcParams['font.family'] = 'AppleGothic' # 맥 지원 한글 폰트
plt.rcParams['axes.unicode_minus'] = False

# -2pi ~ 2pi 사이 100개의 값을 x축 값으로 지정
x = np.linspace(-2 * np.pi, 2*np.pi, 100)
siny = np.sin(x)
cosy = np.cos(x)

# 1행 2열로 분할된 창 중 첫 번째
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x, siny)
plt.grid()
plt.title('sin 함수')

plt.subplot(1,2,2)
plt.plot(x, cosy)
plt.grid()
plt.title('cos 함수')

plt.show()