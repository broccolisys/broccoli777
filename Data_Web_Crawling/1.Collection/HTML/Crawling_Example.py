from bs4 import BeautifulSoup
html = '<td class="title"><div class = "tit3"><a href = "/movie/bi/mi/basic.nhn?code=158191"title="1987">1987</a></div></td>'
# <a title <= 마우스 타겟시 설명 메시지 출력

soup = BeautifulSoup(html, 'html.parser') # 통째로 가지고 와서 통째로 출력
print(soup)
tag = soup.td # td를 가지고 와서 변수처리
print(tag)
tag=soup.div # div 를 가지고 와서 변수처리
print(tag)
tag=soup.a # a를 가지고 와서 변수처리

print(tag)
print(tag.name)
print(tag.attrs)
print(tag.string) # 태그안에 있는 값을 가지고 온다
print(tag.text)    # 태그안에 있는 값을 가지고 온다
