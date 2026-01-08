import pandas as pd
import ast

############
# 정기배송, 생일상 등 특이한 주문 상품번호 필요함-필터링용



naver_1 = pd.read_csv('스마트스토어.csv')
# print(naver_1.head())

# 필요없는 열 삭제
naver = naver_1.drop(['상품주문번호', '배송속성', '풀필먼트사(주문 기준)' ,'클레임상태', '수량클레임 여부', '구매자ID', '구독신청회차', '구독진행회차'], axis=1)

# 결제완료 상태만 추출
naver = naver[naver.주문상태 == '결제완료']

# 정기배송 제외 : 명절 주문만 남기기
naver = naver[naver.상품번호 != 6804137224]
naver = naver[naver.상품번호 != 6804109317]

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


# 배송희망일자, 공동현관비번 분리
    # 숫자만 남긴 채로 엑셀로 변환하면 숫자형 표시가 들쑥날쑥함 : 10.4 ->> 45738 이런 식
    # 그냥 텍스트 그대로 안 자르고 가는 게 나을지도
date_list = []
pw_list = []

for memo in gr_naver['배송희망일자_현관비번'] :
    cut_idx = memo.rfind('/')
    # 배송희망일자
    date_final = memo[:cut_idx].strip()
    cut_idx = date_final.find(':')
    date_final = date_final[cut_idx+1:].strip()
    date_list.append(date_final)

    # 공동현관비번
    pw_final = memo[cut_idx+1:].strip()
    cut_idx = pw_final.find(':')
    pw_final = pw_final[cut_idx+1:].strip()
    pw_list.append(pw_final)

gr_naver['배송일'] = date_list
gr_naver['공동현관비번'] = pw_list


# 옵션+수량 정리
    # 알뜰/정성/...상 기본 구성품도 카운트+1


# 주소, 전화번호


# 판매처 기입
gr_naver['판매처'] = '스마트스토어'


# 파일 추출
gr_naver = gr_naver.drop('옵션정보', axis=1)
gr_naver.to_csv('naver_output.csv', index=False, encoding='utf-8-sig')








item_list = ['탕국', '나물5종', '명태살전',	'동그랑땡',	'부추전', 
             '북어포', '깐밤', '대추', '침조기(중)', '침조기(대)', '민어', '돔', '삼색전', '애호박전',
             '깻잎전', '두부전', '육전', '새우튀김', '오징어튀김', '쥐포튀김', '고구마튀김', '소고기산적',
             '상어산적', '홍합산적', '갈비찜', '잡채', '소불고기', '기타']
# '기타' 항목은 매장 주문 건 메모를 위한 항목, 온라인 주문에서는 접수되지 않을 것을 전제로 함.


# 옵션명 동일한 표기로 전처리
# 주문서에 없어서 표기 모르는 것들은 ## 표시
correction_dict = {
    '탕국 1kg': '탕국',
    '나물5종(500g)': '나물5종',
    '명태살전350g': '명태살전',
    '동그랑땡(1팩에14개)': '동그랑땡',
    '부추전3장': '부추전',
    '북어포1미': '북어포',
    '깐밤100g': '깐밤',
    '건대추130g': '대추',
    '침조기(중)': '침조기(중)',
    '침조기(대)': '침조기(대)',
    '민어': '민어', ##
    '돔': '돔',
    '삼색전4장': '삼색전',
    '애호박전': '애호박전', ##
    '깻잎전380g': '깻잎전',
    '두부전(1모)': '두부전',
    '육전250g': '육전',
    '새우튀김280g': '새우튀김',
    '오징어튀김230g': '오징어튀김',
    '쥐포튀김230g': '쥐포튀김',
    '고구마튀김250g': '고구마튀김',
    '소고기산적': '소고기산적', ##
    '상어산적': '상어산적', ##
    '홍합산적': '홍합산적', ##
    '궁중갈비찜900g': '갈비찜',
    '궁중잡채500g': '잡채',
    '소불고기볶음 350g(+11000원)': '소불고기',
    '소불고기볶음350g': '소불고기',
    '통문어자숙': '통문어자숙', ##
    '빨간고기': '빨간고기',
    '생김치': '생김치', ##
    '나박김치': '나박김치', ##
    '수제식혜900ml': '식혜',
    '민어조기(중)': '민어조기(중)', ##
    '민어조기(소) 3미': '민어조기(소) 3미', ##
    '두부계란전': '두부계란전', ##
    '사과(특)1개(+8000원)': '사과',
    '배(특)1개(+10000원)': '배',
}


def standardize_items(item_list):
    # 항목이 correction_dict에 있다면 바꾸고, 없으면 strip만 해서 두기
    return [correction_dict.get(item.strip(), item.strip()) for item in item_list]


# 표준화 : 리스트 내부 요소별로 correction_dict 적용
gr_naver['옵션정리버전'] = gr_naver['옵션정리버전'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
gr_naver['옵션정리버전'] = gr_naver['옵션정리버전'].apply(standardize_items)


# {항목 : 수량} 딕셔너리 생성
def expand_items_quantities(row):
    items = ast.literal_eval(row['옵션정리버전']) if isinstance(row['옵션정리버전'], str) else row['옵션정리버전']
    quantities = ast.literal_eval(row['수량']) if isinstance(row['수량'], str) else row['수량']

    return dict(zip(items, quantities))




# 옵션 수량 체크
def count_items(df, item_list):
    buyers = df['주문번호'].tolist()
    counts = []
    for row in df.itertuples(index=False):
        # {항목 : 수량} 딕셔너리 생성
        d = expand_items_quantities({'옵션정리버전': getattr(row, '옵션정리버전'), '수량': getattr(row, '수량')})
        # 지정한 item_list 순서대로 수량 리스트 생성, 없는 항목은 0
        counts.append([d.get(item, 0) for item in item_list])
    result = pd.DataFrame(counts, columns=item_list, index=buyers)
    result.index.name = '주문번호'
    return result

counted_naver = count_items(gr_naver, item_list)
counted_naver.to_csv('naver_counted.csv', encoding='utf-8-sig')


# 수량 체크한 버전에 배송 정보 포함한 최종본 엑셀 생성
# gr_naver + counted_naver 데이터프레임 병합 = fin_naver
fin_naver = pd.merge(gr_naver, counted_naver, on='주문번호', how='outer')
fin_naver2 = fin_naver.drop(['주문번호', '상품번호', '수량', '옵션정리버전', '배송희망일자_현관비번'], axis=1)
# fin_naver2['주문자'] = fin_naver2['수령인'] # 자사몰은 주문자=수령인

# 열 순서 변경
# 구매자명,수취인명,배송희망일자_현관비번,배송일,공동현관비번,판매처

all_columns = fin_naver2.columns.tolist()
all_columns.remove('구매자명')
move_cols = ['배송일', '공동현관비번', '판매처']
for col in move_cols:
    all_columns.remove(col)
new_order = ['구매자명'] + all_columns + move_cols
fin_naver2 = fin_naver2[new_order]

fin_naver2.to_csv('naver_final.csv', encoding='utf-8-sig')
