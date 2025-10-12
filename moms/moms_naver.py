import pandas as pd
import re

naver_1 = pd.read_csv('스마트스토어.csv')
# print(naver_1.head())

# 필요없는 열 삭제
naver = naver_1.drop(['상품주문번호', '배송속성', '풀필먼트사(주문 기준)' ,'클레임상태', '수량클레임 여부', '구매자ID', '구독신청회차', '구독진행회차'], axis=1)

# 결제완료 상태만 추출
naver = naver[naver.주문상태 == '결제완료']
# 정기배송 제외 : 명절 주문만 남기기
naver = naver[naver.상품번호 != '6804137224']
naver = naver[naver.상품번호 != '6804109317']

print(naver)

# 주문번호별로 묶기
gr_naver = naver.groupby('주문번호').agg({
    '구매자명' : list,
    '수취인명' : list,
    '상품번호' : list,
    '옵션정보' : list,
    '수량' : list
}).reset_index()

# 중복 내용 삭제-구매자명, 수취인명
gr_naver['구매자명'] = gr_naver['구매자명'].apply(lambda x: list(dict.fromkeys(x)))
gr_naver['수취인명'] = gr_naver['수취인명'].apply(lambda x: list(dict.fromkeys(x)))
gr_naver['상품번호'] = gr_naver['상품번호'].apply(lambda x: list(dict.fromkeys(x)))


# 옵션정보 문자열 정리
order_final = []
dateNpw_final = []
for order_list in gr_naver['옵션정보'] :
    temp = []
    for i in order_list :
        
        # 알뜰상 & 골라담기
        if i.startswith('[') :
            # 비고란 처리 : 처음 ~ 마지막 '/' 이전까지 추출
            # dateNpw : 배송희망일자, 공동현관비번
            cut_idx = i.rfind('/')
            dateNpw = i[:cut_idx].strip()
                
            # 비고란 처리 : 마지막 '/' 이후 골라담기 옵션 추출
            result = i[cut_idx+1:].strip()

            # 단품골라담기, 알뜰상 이름 정리
            if result.startswith('단품') or result.startswith('알뜰상') :
                result = result.split(': ')[1]
            else :
                # 정성상 : 생선 선택란 없음. 전체=비고란으로 처리
                dateNpw = i
                result = '정성상'
                
            temp.append(result)

        # 옵션으로 추가한 메뉴 이름만 추출  
        else :     
            i = i.split(': ')[1]
            temp.append(i)

    dateNpw_final.append(dateNpw)
    order_final.append(temp)

gr_naver['옵션정리버전'] = order_final
gr_naver['배송희망일자_현관비번'] = dateNpw_final


# 옵션+수량 정리




# 파일 추출
print(gr_naver)
gr_naver.to_csv('output.csv', index=False, encoding='utf-8-sig')
