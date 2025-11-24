import pandas as pd
import ast

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



# 판매처 기입
gr_hada['판매처'] = '자사몰'

# 중간 파일 추출
gr_hada = gr_hada.drop('주문상품명(옵션포함)', axis=1)
gr_hada.to_csv('hada_output.csv', index=False, encoding='utf-8-sig')


# 옵션+수량 정리 : moms_fun.py
    # 기존 리스트부터 카운트
    # 알뜰/... 상 키값도 따로 : 알뜰상(상 이름 + 생선종류) 분리 필요
    # 알뜰/정성/...상 기본 구성품을 기존 리스트에서 검색, 중복되는 항목은 카운트+1
    # 알뜰/... 상 이름은 리스트에서 제거 --> 최종 품목+수량 리스트와 최초 주문 리스트 같이 준비해야 안 헷갈릴 듯


# 여기서 output 파일을 다시 읽어서 데이터프레임을 새로 갖고 오는 게 나을까
# 원래 gr_hada를 계속 사용하는 게 나을까 <<
# hop = pd.read_csv('hada_output.csv')


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
gr_hada['옵션정리버전'] = gr_hada['옵션정리버전'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
gr_hada['옵션정리버전'] = gr_hada['옵션정리버전'].apply(standardize_items)


# {항목 : 수량} 딕셔너리 생성
def expand_items_quantities(row):
    items = ast.literal_eval(row['옵션정리버전']) if isinstance(row['옵션정리버전'], str) else row['옵션정리버전']
    quantities = ast.literal_eval(row['수량']) if isinstance(row['수량'], str) else row['수량']

    return dict(zip(items, quantities))



#### 알뜰상, 정성상, 고급상 -> 전처리 과정에서 수량 추가 필요함
# 상이 있으면 {항목 : 수량} 딕셔너리 하나 더 추가해서 기존 옵션 수량에 + 해주기

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

counted_hada = count_items(gr_hada, item_list)
counted_hada.to_csv('hada_counted.csv', encoding='utf-8-sig')


# 수량 체크한 버전에 배송 정보 포함한 최종본 엑셀 생성
# gr_hada + counted_hada 데이터프레임 병합 = fin_hada
fin_hada = pd.merge(gr_hada, counted_hada, on='주문번호', how='outer')
fin_hada2 = fin_hada.drop(['주문번호', '상품번호', '수량', '옵션정리버전'], axis=1)
fin_hada2['주문자'] = fin_hada2['수령인'] # 자사몰은 주문자=수령인

all_columns = fin_hada2.columns.tolist()
all_columns.remove('주문자')
move_cols = ['수령인 우편번호', '수령인 주소', '수령인 상세 주소', '배송메시지', '수령인 휴대전화', '판매처']
for col in move_cols:
    all_columns.remove(col)
new_order = ['주문자'] + all_columns + move_cols
fin_hada2 = fin_hada2[new_order]

fin_hada2.to_csv('hada_final.csv', encoding='utf-8-sig')

