# 실습1
a = float(input("첫번째 숫자 입력 : "))
b = float(input("두번쩨 숫자 입력 : "))

print("---------------")
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
print(a, "/", b, "=", a/b)
print("---------------")


# 포맷 코드
a = int(input("첫번째 숫자 입력 : "))
b = int(input("두번째 숫자 입력 : "))

print('%d + %d = %+10d' % (a, b, a+b))
print('%d - %d = %+10d' % (a, b, a-b))
print('%d * %d = %+10d' % (a, b, a*b))
print('%d / %d = %+10.2f' % (a, b, a/b))


# f문자열
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))

avg = (kor + eng + math)/3

print('\n---------------------\n')
print(f'국어 = {kor}, 영어 = {eng}, 수학 = {math}')
print(f'\n => 평균 : {avg:.2f}')



# 사칙계산기
msg = '''
      <사칙연산기>
-------------------------
(1) +, -, *, / 만 가능
(2) 양의 정수만 가능
(3) 단일 연산만 가능
-------------------------'''
print(msg)
exp = input("\n수식을 입력하세요 (예:10+20) : ")
exp = exp.replace(' ', '') # 공백 삭제

if exp.count('+') == 1 :
    s1, s2 = exp.split('+')
    if s1.isdigit() and s2.isdigit() :
        s1 = int(s1)
        s2 = int(s2)
        print(f'\n{s1} + {s2} = {s1+s2}')

if exp.count('-') == 1 :
    s1, s2 = exp.split('-')
    if s1.isdigit() and s2.isdigit() :
        s1 = int(s1)
        s2 = int(s2)
        print(f'\n{s1} - {s2} = {s1-s2}')

if exp.count('*') == 1 :
    s1, s2 = exp.split('*')
    if s1.isdigit() and s2.isdigit() :
        s1 = int(s1)
        s2 = int(s2)
        print(f'\n{s1} * {s2} = {s1*s2}')

if exp.count('/') == 1 :
    s1, s2 = exp.split('/')
    if s1.isdigit() and s2.isdigit() :
        s1 = int(s1)
        s2 = int(s2)
        print(f'\n{s1} / {s2} = {s1/s2:.2f}')
