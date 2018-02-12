from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html,"html.parser") # 처음 나타난 태그를 찾아냄
nameList = bs0bj.findAll("span",{"class":"green"}) # 페이지의 태그 전체를 찾음
for name in nameList: # 리스트의 모든 이름 순회
    print(name.get_text()) # 태그를 제외하고 콘텐츠만 출력

# get_text()는 현재 문서에서 모든 태그를 제거하고 텍스트만 있는 문자열 반환
# 특히 get_text()는 항상 마지막, 최종 데이터를 출력하거나 저장, 조작하기 직전에만 사용용