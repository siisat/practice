# 실습2
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

while 1 :
    page = input('가져올 페이지 번호 입력 : ')
    if not page.isdigit() : continue
    if 1 <= int(page) <= 12 : break


# 입력 받은 페이지로 연결
doc = urlopen('https://www.pusan.ac.kr/kor/CMS/Board/Board.do?robot=Y&mCode=MN095&mgr_seq=3&page=' + page) 
htmldoc = bs(doc, 'html.parser')

sel = htmldoc.select('#board-wrap > div.board-list-wrap > table > tbody > tr')

fp = open('공지사항.csv', 'w', encoding='utf-8')
print('번호,제목,작성자,작성일자,조회수', file=fp)

for tr in sel :
    # tr.select_one() : 클래스 정보 1개 반환, 클래스명 : '.~~~'
    # .strip() : 공백 제거
    num = tr.select_one('.num').text.strip()
    if num == '' : num = '공지'
    subject = tr.select_one('.subject').text.strip().replace(',', '/')
    writer = tr.select_one('.writer').text
    date = tr.select_one('.date').text
    cnt = tr.select_one('.cnt').text

    res = num + ',' + subject + ',' + writer + ',' + date + ',' + cnt
    print(res, file=fp)

fp.close()