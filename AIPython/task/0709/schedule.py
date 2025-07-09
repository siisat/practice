# 실습1
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

doc = urlopen('https://www.pusan.ac.kr/kor/CMS/Haksailjung/view.do?mCode=MN076')
htmldoc = bs(doc, 'html.parser')
# print(htmldoc)

# 개발자도구에서 copy>copy selector
sel = htmldoc.select('#cont > div.acacal-diaWr > div > table > tbody > tr')
print(sel[0])

fp = open('학사일정.csv', 'w')
print('일정,내용', file=fp) # 학사일정 파일 1행에 내용 입력

for tr in sel :
    # .find('th') : th 태그를 찾아서 -> .text : 텍스트만 추출
    sche = tr.find('th').text # 일정
    cont = tr.find('td').text.replace(',', '/') # 내용
    print(sche + ',' + cont, file=fp)

fp.close()