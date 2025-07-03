# 실습1
import mymod as m

while 1 :
    try :
        score = input('국어, 영어, 수학 점수를 입력하세요 : ').split()
        score = [int(n) for n in score]
        if len(score) != 3 : continue
        if any (n<0 or n>100 for n in score) : continue
        break
    except :
        pass

avg = m.average(score[0], score[1], score[2])
grd = m.grade(avg)

print('\n----------')
print(f'평균 : {avg:.2f}')
print(f'학점 : {grd}')
print('\n----------')


# 실습2
h = float(input('키를 입력하세요 : '))
w = float(input('몸무게를 입력하세요 : '))
bmi, res = m.obesity(h, w)

print('\n---------------\n')
print(f'BMI : {bmi:.2f}')
print('비만도 : ', res)
print('\n---------------')


# 실습3
from mymod import fibonacci # 함수 하나만 import

cnt = int(input('피보나치 수열의 항 개수를 입력하세요 : '))
print('------------------------\n')

fibo = fibonacci(cnt)
for i, item in enumerate(fibo) :
    print(f'{item:<15d}', end='')
    if (i+1)%5 == 0 : print()

print('\n------------------------')


# 실습4
import random as rd
import datetime

def test() :
    su1 = rd.randint(0,9)
    su2 = rd.randint(0,9)
    op = rd.choice(['+', '-', '*'])

    p = str(su1) + ' ' + op + ' ' + str(su2)
    return p

paper = []
d = datetime.date.today()
print('<수학 시험 : 5문제>\n')
paper.append('오늘 날짜 : ' + str(d))
score = 0

for n in range(1,6) :
    prob = test() # prob = 문자열 형태의 수식
    cor = eval(prob) # cor = 수식의 계산 결과(정답)-eval() 활용

    que = f'({n}번) {prob} = '
    ans = input(que) # 사용자 : 문제에 대한 정답 입력

    if str(cor) == ans :
        score += 10
        paper.append(que + ans + ' (O)')
    else :
        paper.append(que + ans + ' (X)')

paper.append(f'\n => 점수 : {score}점')
print('\n------------------')
print(' <시험지> ')

for item in paper :
    print(item)