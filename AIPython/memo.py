def solution(numer1, denom1, numer2, denom2):
#     if denom1 <= denom2 :
#         n1 = numer1
#         d1 = denom1
#         n2 = numer2
#         d2 = denom2
#     elif denom1 > denom2 :
#         n1 = numer2
#         d1 = denom2
#         n2 = numer1
#         d2 = denom1
    
#     if d2%d1 == 0 :
#         n3 = n1*(d2//d1) + n2
#         d3 = d2
#     else :
#         d3 = d1*d2
#         n3 = n1*(d3//d1) + n2*(d3//d2)
    
    d3 = denom1*denom2
    n3 = numer1*denom2 + numer2*denom1
    
    # 최대공약수
    list_d3 = [i for i in range(1,d3+1) if d3%i==0]
    list_n3 = [i for i in range(1,n3+1) if n3%i==0]
    
    list_m = [i for i in list_d3 if i in list_n3][-1] # [-1] : 이게 뭘까
    print(list_m)

    # 약분
    # i = 2
    # while i<=n3 and i<=d3 :
    #     if n3%i == 0 and d3%i == 0 :
    #         n3 = n3//i
    #         d3 = d3//i
    #     if n3 == 1 or d3 == 1 : break
    #     i += 1
        
    answer = [n3/list_m, d3/list_m]
    return answer

solution(5, 20, 15, 25)