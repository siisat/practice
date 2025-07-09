# 실습3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

fp = open('취업정보.csv', 'w', encoding='utf-8')
print('번호,상태,회사명,채용정보,채용상태,마감일,조회수', file=fp)


for page in range(1,11) : # page = int형, url에 넣을 땐 str으로 변환
    doc = urlopen('https://job.pusan.ac.kr/ko/recruit/board/list/' + str(page))
    htmldoc = bs(doc, 'html.parser')

    sel = htmldoc.select('#ModuleWorkingWorkList > div.work > div > ul > li')
    sel = sel[1:]

    for li in sel :
        num = li.select_one('.loopnum').text.strip()
        status = li.select_one('.status').text
        name = li.select_one('.co>.tit').text.strip().replace(',', ' ')
        info = li.select_one('.subject>.tit').text.strip().replace(',', '/')
        type_info = li.select_one('.subject>.sub_tit>.recruit_type').text
        deadline = li.select_one('.end_date').text.strip()
        deadline = deadline[0:10] + ' ' + deadline[10:] # 날짜와 시간 사이 공백 추가
        cnt = li.select_one('.view').text

        res = num + ',' + status + ',' + name + ',' + info + ',' + type_info + ',' + deadline + ',' + cnt
        print(res, file=fp)

fp.close()
