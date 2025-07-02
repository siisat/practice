# 실습1-(1)

while 1 :
    try :
        # 입력값을 .split() 으로 자르면 리스트로 반환
        score = input('심사점수 5개 입력(공백 구분) : ').split()
        score = [int(n) for n in score] # 리스트 항목을 정수로 변환
        if len(score) == 5 : break # 입력값 5개로 제한
    except :
        pass

score.remove(max(score))
score.remove(min(score))

print('\n---------------------\n')
print('심사평점 : ', sum(score)/3)
print('\n---------------------\n')


# 실습1-(2)
import random as rd

gr1 = []
for n in range(9) :
    gr1.append(rd.randint(20,50))

gr2 = [rd.randint(20,50) for n in range(9)]

print('(그룹-1)심사점수 : ', gr1)
print('(그룹-2)심사점수 : ', gr2)

gr1.sort()
gr2.sort()
score = gr1[2:7] + gr2[2:7]
score.sort()

print('\n---------------------\n')
print('유효점수 : ', score)
print('심사평점 : ', sum(score)/len(score))
print('\n---------------------\n')


# 실습2
import random as rd

score = [rd.randint(20,100) for n in range(50)]

print('\n--------<번호순으로 출력>--------\n')
for n in range(len(score)) :
    # 출력 양식 : (번호)점수
    print(f'({n+1}){score[n]}', end=' ')
print('\n---------------------\n')

score2 = score.copy()
score2.sort(reverse=True) # 내림차순 정렬 .sort(reverse=True)
print('전체 평점 : ', sum(score2)/len(score2))
print('상위-10명의 평점 : ', sum(score2[0:10])/10)
print('하위-10명의 평점 : ', sum(score2[-10:])/10)

cnt = score.count(100) # 리스트 내 값이 100인 항목의 개수 카운트 .count(100)
print(f'\n100점 인원수 {cnt}명', end=' ')

if cnt > 0 :
    print('(', end='')
    for n in range(len(score)) :
        if score[n] == 100 :
            print(f'{n+1}번', end=' ')
    print(')')


# 실습3
import random as rd

allstu = []
for n in range(20) :
    stuid = n+1
    kor = rd.randint(20,100)
    eng = rd.randint(30,100)
    math = rd.randint(10,100)
    avg = round( (kor+eng+math)/3, 1)
    if avg >= 80 : grade = '우수'
    elif avg >= 60 : grade = '보통'
    else : grade = '미흡'

    allstu.append([stuid, kor, eng, math, avg, grade])

print('-'*50)
print('번호\t 국어\t 영어\t 수학\t 평균\t 학점')
print('-'*50)
for stu in allstu :
    print(f'{stu[0]:03d}\t {stu[1]}\t {stu[2]}\t {stu[3]}\t {stu[4]}\t {stu[5]}\t')
print('-'*50)

#
print('-'*50)
print('번호\t 국어\t 영어\t 수학\t 평균\t 학점')
print('-'*50)
for stu in allstu :
    for line in stu :
        print(f'{line}', end='\t')
    print()
print('-'*50)


# 실습4
money = {10000:'만  원', 5000:'오천원', 1000:'천  원', 500:'오백원', 100:'백  원'}

mon = int(input('투입한 금액을 입력하세요 : '))
sec1 = int(input('1구간 표의 개수 입력 : '))
sec2 = int(input('2구간 표의 개수 입력 : '))
change = mon - (sec1*1300 + sec2*1500)

print('\n-------------------\n')
print('거스름돈 : %d 원\n' %change)

if change < 0 :
    print('%d 원이 부족합니다.' %-change)

for k, v in money.items() :
    if change//k > 0 :
        # print('%s : %d 개' %(v, (change//k)))
        print(f'{v} : {change//k} 개')
        change %= k # change = change % 10000

print('\n-------------------\n')


# 실습5
import random as rd

allstu = {} # 학생 정보 20개

for n in range(20) :
    # key가 중복되어 생성되는 경우 딕셔너리에 항목이 추가되지 않음
    stuid = rd.randint(1000,1999) # 학번-key
    kor = rd.randint(20,100)
    eng = rd.randint(30,100)
    math = rd.randint(10,100)
    avg = round( (kor+eng+math)/3, 1)
    if avg >= 80 : grade = '우수'
    elif avg >= 60 : grade = '보통'
    else : grade = '미흡'

    val = [kor, eng, math, avg, grade] # value
    allstu[stuid] = val # 딕셔너리 항목 추가 : 딕셔너리[key] = value

for stu in allstu.items() :
    print(stu)

print('\n인원수 : ', len(allstu))

while 1 :
    id = input('\n검색할 학번을 입력하세요(0 입력시, 종료) : ')
    if not id.isdigit() : continue
    if id == '0' : break
    id = int(id)

    print('\n-------------------')
    # print('국어/영어/수학/평균/학점 : ', allstu[id])
    # 이 경우 존재하지 않는 id로 검색 시 에러 발생
    print('국어/영어/수학/평균/학점 : ', allstu.get(id, '없는 학번입니다.'))
    print('-------------------')
