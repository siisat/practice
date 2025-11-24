

# 알뜰상 구성
al_set = ['탕국', '명절나물', '동그랑땡', '삼색전', '명태살전', '북어포', '깐밤', '대추']
# 여기에 생선 선택 1 : 침조기(중), 돔, 민어


# 정성상 구성
jung_set = ['탕국', '탕국', '명절나물', '명절나물', '침조기(중)', '동그랑땡', '삼색전', '명태살전', '부추전', '두부전', '오징어튀김', '새우튀김', '고구마튀김', '북어포', '깐밤', '대추']

# 고급상 구성
go_set = ['탕국', '탕국', '탕국', '명절나물', '명절나물', '침조기(중)', '돔', '민어', '통문어자숙', '궁중갈비찜', '궁중잡채', '동그랑땡', '삼색전', '명태살전', '육전', '육전', '부추전', '깻잎전', '소고기산적', '홍합산적', '상어(돔배기)산적', '오징어튀김', '새우튀김', '쥐포튀김', '고구마튀김', '두부전', '생김치', '북어포', '깐밤', '대추', '식혜']





import pandas as pd
import ast

hop = pd.read_csv('hada_output.csv')

# ['건대추130g', '고구마튀김250g', '궁중갈비찜900g', '궁중잡채500g', '깐밤100g', '깻잎전380g', '나물5종(500g)', '돔', '동그랑땡(1팩에14개)',
# '두부전(1모)', '명태살전350g', '배(특)1개(+10000원)', '부추전3장', '북어포1미', '빨간고기', '사과(특)1개(+8000원)', '삼색전4장', '새우튀김280g',
# '소불고기볶음 350g(+11000원)', '소불고기볶음350g', '수제식혜900ml', '오징어튀김230g', '육전250g', '정성', '제사상_알뜰 (생선 기본제공/택1)=침조기(중)',
# '쥐포튀김230g', '침조기(대)', '침조기(중)', '탕국 1kg']

# 탕국,나물5종,명태살전,동그랑땡,부추전,북어포,깐밤,대추,침조기(중),침조기(대),민어,돔,삼색전,애호박전	
# 깻잎전,두부전,육전,새우튀김,오징어튀김,쥐포튀김,고구마튀김,소고기산적,상어산적,홍합산적,갈비찜,잡채,소불고기	
# 통문어자숙,빨간고기,생김치,나박김치,식혜,민어조기(중),민어조기(소) 3미,두부계란전,사과,배


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

# 항목명 표준화 예시
def standardize_items(item_list):
    # 각 항목명이 correction_dict에 있다면 바꾸고, 없으면 strip만 해서 둡니다
    return [correction_dict.get(item.strip(), item.strip()) for item in item_list]

hop['옵션정리버전'] = hop['옵션정리버전'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
# 이제 표준화 작업: 리스트 내부 요소별로 correction_dict 적용!
hop['옵션정리버전'] = hop['옵션정리버전'].apply(standardize_items)



# {항목 : 수량} 딕셔너리 생성
def expand_items_quantities(row):
    items = ast.literal_eval(row['옵션정리버전']) if isinstance(row['옵션정리버전'], str) else row['옵션정리버전']
    quantities = ast.literal_eval(row['수량']) if isinstance(row['수량'], str) else row['수량']

    return dict(zip(items, quantities))


# 1
# 상품 리스트를 주문 항목과 대조하여 최신화*반복
# def count_items(df):
#     item_set = set()
#     buyers = df['주문번호'].tolist()

#     for row in df.itertuples(index=False):
#         items = ast.literal_eval(getattr(row, '옵션정리버전')) if isinstance(getattr(row, '옵션정리버전'), str) else getattr(row, '옵션정리버전')
#         item_set.update(items)

#     item_list = sorted(list(item_set))
#     counts = []

#     for row in df.itertuples(index=False):
#         d = expand_items_quantities({'옵션정리버전': getattr(row, '옵션정리버전'), '수량': getattr(row, '수량')})
#         counts.append([d.get(item, 0) for item in item_list])

#     result = pd.DataFrame(counts, columns=item_list, index=buyers)
#     result.index.name = '주문번호'

#     return result

# result_hop = count_items(hop)
# print(result_hop)
# result_hop.to_csv('hada_fin.csv', encoding='utf-8-sig')


#2
# 상품 리스트가 존재할 때, 리스트와 비교해서 수량 체크만

#### 알뜰상, 정성상, 고급상 -> 전처리 과정에서 수량 추가 필요함
# 상이 있으면 {항목 : 수량} 딕셔너리 하나 더 추가해서 기존 옵션 수량에 + 해주기

def count_items(df, item_list):
    buyers = df['주문번호'].tolist()
    counts = []
    for row in df.itertuples(index=False):
        d = expand_items_quantities({'옵션정리버전': getattr(row, '옵션정리버전'), '수량': getattr(row, '수량')})
        # 지정한 item_list 순서대로 수량 리스트 생성, 없는 항목은 0
        counts.append([d.get(item, 0) for item in item_list])
    result = pd.DataFrame(counts, columns=item_list, index=buyers)
    result.index.name = '주문번호'
    return result

counted_hada = count_items(hop, item_list)
counted_hada.to_csv('hada_counted.csv', encoding='utf-8-sig')




