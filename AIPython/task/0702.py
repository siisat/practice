# 실습1-(1)

# while 1 :
#     try :
#         # 입력값을 .split() 으로 자르면 리스트로 반환
#         score = input('심사점수 5개 입력(공백 구분) : ').split()
#         score = [int(n) for n in score] # 리스트 항목을 정수로 변환
#         if len(score) == 5 : break # 입력값 5개로 제한
#     except :
#         pass

# score.remove(max(score))
# score.remove(min(score))

# print('\n---------------------\n')
# print('심사평점 : ', sum(score)/3)
# print('\n---------------------\n')


# 실습1-(2)
# import random as rd

# gr1 = []
# for n in range(9) :
#     gr1.append(rd.randint(20,50))

# gr2 = [rd.randint(20,50) for n in range(9)]

# print('(그룹-1)심사점수 : ', gr1)
# print('(그룹-2)심사점수 : ', gr2)

# gr1.sort()
# gr2.sort()
# score = gr1[2:7] + gr2[2:7]
# score.sort()

# print('\n---------------------\n')
# print('유효점수 : ', score)
# print('심사평점 : ', sum(score)/len(score))
# print('\n---------------------\n')


# 실습3
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