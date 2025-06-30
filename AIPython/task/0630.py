# 실습1
money = int(input('투입한 금액을 입력하세요 : '))
sec1 = int(input('1구간 표의 개수 입력 : '))
sec2 = int(input('2구간 표의 개수 입력 : '))
change = money - (sec1*1300 + sec2*1500)

print('\n-------------------\n')
print('거스름돈 : %d 원\n' %change)

if change < 0 :
    print('%d 원이 부족합니다.' %-change)

if change//10000 > 0 :
    print('만 원 : %d 개' %(change//10000))  # 변수 출력 시 연산이 필요한 경우 ()안에 입력
    change %= 10000 # change = change % 10000

if change//1000 > 0 :
    print('천 원 : %d 개' %(change//1000))
    change %= 1000

if change//100 > 0 :
    print('백 원 : %d 개' %(change//100))
    change %= 100

if change//10 > 0 :
    print('십 원 : %d 개' %(change//10))


print('\n-------------------\n')


# 실습2
hei = float(input('키를 입력하세요 : '))
wei = float(input('몸무게를 입력하세요 : '))
bmi = (wei*10000)/hei**2

# 에러 발생 예시
# if bmi <= 19 : res = '저체중'
# if bmi <= 24 : res = '정상'
# if bmi <= 19 : res = '과체중'
# if bmi > 29 : res = '비만'

if bmi <= 19 : res = '저체중'
if 19 < bmi <= 24 : res = '정상'
if 24 < bmi <= 29 : res = '과체중'
if bmi > 29 : res = '비만'

print('\n-------------------\n')
print(f'BMI : {bmi:.4f}\n')
print(f'비만도 : {res}')
print('\n-------------------\n')


# 실습3
su = input('>> 숫자 1개를 입력하세요 : ')
su = su.replace(' ', '') # 공백 미포함으로 변환

if su == '0' or su == '-0' or su == '0.0' or su == '-0.0' :
    print('\n 0 입니다.')
elif su.isdigit() :
    print(f'\n {su} : 양의 정수입니다.')
elif su[0] == '-' and su[1:].isdigit() :
    print(f'\n {su} : 음의 정수입니다.')
elif su.count('.') == 1 :
    if su.replace('.', '').isdigit() :
        print(f'\n {su} : 양의 실수입니다.')
    elif su[0] == '-' and su[1:].replace('.', '').isdigit() :
        print(f'\n {su} : 음의 실수입니다.')
    else :
        print(f'\n {su} : 숫자가 아닙니다.')
else :
        print(f'\n {su} : 숫자가 아닙니다.')


# 실습4
import random as rd

print('\n <철수/컴퓨터 가위바위보> \n')
num = input('철수 가위바위보 번호 선택(가위: 1, 바위: 2, 보: 3) : ')

if num == '1' :
    sel = '가위'
    num = 1
elif num == '2' :
    sel = '바위'
    num = 2
elif num == '3' :
    sel = '보'
    num = 3
else :
    sel = '***'
    num = 0

c_num = rd.randint(1,3)
if c_num == 1 : c_sel = '가위'
if c_num == 2 : c_sel = '바위'
if c_num == 3 : c_sel = '보'

print('\n----------------------\n')

print(f'철수 : {sel}, 컴퓨터 : {c_sel}')

if num == 0 :
    print('\n\n=> 철수가 [오류]입니다.')

if num == c_num :
    print('\n\n=> 비겼습니다.')

if (num == 1 and c_num == 3) or (num == 2 and c_num == 1) or (num == 3 and c_num == 2) :
    print('\n\n=> 철수가 이겼습니다.')

if (num == 1 and c_num == 2) or (num == 2 and c_num == 3) or (num == 3 and c_num == 1) :
    print('\n\n=> 컴퓨터가 이겼습니다.')

print('\n----------------------\n')