# 실습1
def average (*su) : # * : 튜플 객체
    res = sum(su)/len(su)
    return res

def grade (jumsu) :
    if jumsu >= 80 : return '우수'
    elif jumsu >= 60 : return '보통'
    else : return '미흡'


# 실습2
def obesity (hei, wei) :
    bmi = (wei * 10000) / hei**2
    if bmi < 18.5 : res = '저체중'
    elif bmi < 23 : res = '정상'
    elif bmi < 25 : res = '과체중'
    else : res = '비만'

    return (bmi, res)


# 실습3
def fibonacci (num) :
    if num < 1 : return []
    if num == 1 : return [1]
    if num == 2 : return [1, 1]

    fibo = [1, 1]
    for n in range(2,num) :
        fibo.append(fibo[n-2]+fibo[n-1])
    
    return fibo
