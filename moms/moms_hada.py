import pandas as pd

############
# 정기배송, 생일상 등 특이한 주문 상품번호 필요함-필터링용

# 원본 : hada_1
hada_1 = pd.read_csv('hada.csv')

# 필요없는 열 삭제
hada = hada_1.drop(['쇼핑몰', '쇼핑몰번호', '품목별 주문번호', '총 주문금액', '총 결제금액', '주문상품명', '판매가', '결제구분', '결제수단', '발주일', '배송국가'], axis=1)

# # 결제완료 상태만 추출 : 취소 건은 안 뜨는 듯

# 정기배송 제외 : 명절 주문만 남기기
hada = hada[hada.상품번호 != 19]

# 주문번호별로 묶기
gr_hada = hada.groupby('주문번호').agg({
    '수령인' : list,
    '수령인 휴대전화' : list,
    '수령인 우편번호' : list,
    '수령인 주소' : list,
    '수령인 상세 주소' : list,
    '배송메시지' : list,
    '상품번호' : list,
    '주문상품명(옵션포함)' : list,
    '수량' : list
}).reset_index()

# # 중복 내용 삭제
gr_hada['수령인'] = gr_hada['수령인'].apply(lambda x: list(dict.fromkeys(x)))
gr_hada['수령인 휴대전화'] = gr_hada['수령인 휴대전화'].apply(lambda x: list(dict.fromkeys(x)))
gr_hada['수령인 우편번호'] = gr_hada['수령인 우편번호'].apply(lambda x: list(dict.fromkeys(x)))
gr_hada['수령인 주소'] = gr_hada['수령인 주소'].apply(lambda x: list(dict.fromkeys(x)))
gr_hada['수령인 상세 주소'] = gr_hada['수령인 상세 주소'].apply(lambda x: list(dict.fromkeys(x)))
gr_hada['배송메시지'] = gr_hada['배송메시지'].apply(lambda x: list(dict.fromkeys(x)))
gr_hada['상품번호'] = gr_hada['상품번호'].apply(lambda x: list(dict.fromkeys(x)))



# # 옵션정보 문자열 정리
order_final = []
dateNpw_final = []
for order_list in gr_hada['주문상품명(옵션포함)'] :
    temp = []
    for i in order_list :
        
        # 알뜰상
        if i.startswith('[ 사전예약 ] 제사상_알뜰') :
            # 비고란 처리 : 처음 '(' 부터 끝까지 추출
            cut_idx = i.find('(')
            result = i[cut_idx+1:].strip()
            result = result[:-1] # 마지막 ')'만 삭제

            # 비고란 처리 : 알뜰상에 단품 추가한 경우 옵션만 추출
            if ',' in result :
                cut_idx = i.rfind('=')
                result = i[cut_idx+1:].strip()
                result = result[:-1]

        # 정성상 & 골라담기 : 옵션으로 추가한 메뉴 이름만 추출  
        else :     
            cut_idx = i.rfind('=')
            result = i[cut_idx+1:].strip()
            result = result[:-1]

        temp.append(result)

    order_final.append(temp)

gr_hada['옵션정리버전'] = order_final

# # 옵션+수량 정리
#     # 알뜰/정성/...상 기본 구성품도 카운트+1


# 판매처 기입
gr_hada['판매처'] = '자사몰'


# # 파일 추출
gr_hada = gr_hada.drop('주문상품명(옵션포함)', axis=1)
gr_hada.to_csv('hada_output.csv', index=False, encoding='utf-8-sig')
