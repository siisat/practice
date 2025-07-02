# 실습1-(1)
dan = int(input('구구단 몇 단을 출력할까요? : '))

print('\n----------------\n')
for su in range(1,10) :
    print(f'{dan}*{su}={dan*su}')
print('\n----------------\n')


# 실습1-(2)
print('\n----------------------------\n')
for su in range(1,10) :
    for dan in range(2,10) :
        print(f'{dan}*{su}={dan*su:<2d}', end=' ')
        # :<2d = 왼쪽부터 정렬, :2d = 오른쪽부터 정렬
    print()
print('\n----------------------------\n')


# 실습2
num = int(input('양의 정수를 입력하세요 : '))

print(f'<{num}의 약수>')
for n in range(1,num+1) :
    if num%n == 0 :
        print(n, end=' ')

print()

for n in range(1,num) :
    if num%n == 0 :
        print(n, end=', ')
print(num)


# 실습3
num1, num2 = input('2개의 정수를 입력하세요 : ').split(' ')
num1 = int(num1)
num2 = int(num2)

ran1 = min(num1, num2)
ran2 = max(num1, num2)

print('\n----------------------------\n')
t_count = 0
for n in range(ran1,ran2+1) :
    count = 0
    for k in range(1,n+1) :
        if n%k == 0 :
            count += 1
    if count == 2 :
        t_count += 1
        print(f'{n:4d}', end=' ')
        if t_count%10 == 0 : print()

print(f'\n\n소수의 개수 : {t_count} 개')
print('----------------------------\n')

# 필기
primecnt = 0
for su in range(ran1,ran2+1) :
    if su < 2 : continue
    cnt = 0 #su의 약수 개수
    for n in range(1,su+1) :
        if su%n == 0 : cnt += 1
        if cnt > 2 : break
    if cnt == 2 :
        print(f'{su:4d}', end=' ')
        primecnt += 1
        if primecnt%10 == 0 : print()

print(f'\n\n소수의 개수 : {primecnt} 개')
print('----------------------------\n')


# while-실습1
dan = int(input('구구단 몇 단을 출력할까요? : '))
su = 1

print('\n----------------\n')
while su < 9 :
    print(f'{dan}*{su}={dan*su}')
    su += 1
print('\n----------------\n')


# 실습4
# for문의 range 범위에는 정수 목록만 포함 가능
# -> 실수 등차수열을 표현하려면 while문 사용
ran1 = float(input('첫재항을 입력하세요 : '))
d = float(input('공차를 입력하세요 : '))
ran2 = float(input('최대항을 입력하세요 : '))

print('\n---------------------')
if d > 0 :
    while ran1 <= ran2 :
        print(ran1, end=' ')
        ran1+=d
elif d < 0 :
    while ran1 >= ran2 :
        print(ran1, end=' ')
        ran1+=d
print('\n---------------------\n')

# 필기
while 1 : # 무한루프
    if d == 0 : break
    if d > 0 and ran1 > ran2 : break
    if d < 0 and ran1 < ran2 : break

    print(ran1, end=' ')
    ran1 += d


# 오류처리
while 1 :
    try :
        ran1 = float(input('첫재항을 입력하세요 : '))
        d = float(input('공차를 입력하세요 : '))
        ran2 = float(input('최대항을 입력하세요 : '))
        break 
    except :
        print('--------')


while 1 :
    try :
        dan = int(input('구구단 몇 단을 출력할까요? : '))
        if dan >=2 : break
    except :
        pass

while 1 :
    try :
        su1, su2 = input('정수 2개')
        su1 = int(su1)
        su2 = int(su2)
        break
    except :
        pass