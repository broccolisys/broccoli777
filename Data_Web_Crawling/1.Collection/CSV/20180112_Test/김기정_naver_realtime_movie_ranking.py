import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# print(soup.prettify())

result_movie = []
result_updown = []
result_total = []

movie_trs =  soup.findAll('div', attrs={'class':'tit3'}) # div class의 속성의 tit3 관련된 것을 뽑는다.
updown_trs =  soup.findAll('td', attrs={'range ac'}) # td class의 속성의 range ac 관련된 것을 뽑는다.

if (movie_trs): # movie_trs 만 해당
    for movie_tr in movie_trs: # for 문을 이용해서 하나씩 뽑는다
        movie_tag = list(movie_tr.strings) # list 로 묶어 준뒤
        movie_name = movie_tag[1] # 그 중 영화명에 관련된 것만 변수 저장
        result_movie.append([movie_name]) # append 함수 이용해서 보관


if (updown_trs): # updown_trs만 해당
    for updown_tr in updown_trs: # for 문을 이용해서 하나씩 뽑는다
        updown_tag = list(updown_tr.strings) # list로 묶어준 뒤
        updown_name = updown_tag[0] # 그 중 updown에 관련된 것만 변수 저장
        result_updown.append([updown_name]) # append 함수 이용해서 보관

for i in range(len(result_movie)): # for 문을 이용해서, 앞에 넘버링 해준다.
    if i == 0: # 초기에는 반드시 1이 와야 하므로, i가 0이 온다면
        total_data = [1] + result_movie[i] + result_updown[i] # 1값을 포함시켜서 같이 저장 시키면, 다음에 1이 먼저 오게된다.
        result_total.append(total_data)
    else:
        total_data = [i+1] + result_movie[i] + result_updown[i] # 다음부터는 2,3,4,가 와야하므로 i+1로 저장
        result_total.append(total_data)

movie_table = DataFrame(result_total, columns=('순위', '영화명', '변동폭'))
movie_table.to_csv('movie_ranking_bigdata.csv', encoding="cp949", mode='w', index=False)

