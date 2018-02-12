import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
result = []
result2 = []
result3 = []
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

movie_trs = soup.find_all('div', attrs = {'class':'tit3'},)
range_trs = soup.find_all('td', attrs = {'range ac'})

if (movie_trs):
    for movie_tr in movie_trs:
        tr_tag = list(movie_tr.strings)
        movie_name = tr_tag[1]
        result.append([movie_name])

if (range_trs):
    for range_tr in range_trs:
        tr_tag2 = list(range_tr.strings)
        movie_range = tr_tag2[0]
        result2.append([movie_range])

for i in range(len(result)):
    if i == 0:
     total_result= [1]+ result[i]+result2[i]
     result3.append(total_result)
    else:
        total_result = [i+1] + result[i] + result2[i]
        result3.append(total_result)

movie_table = DataFrame(result3, columns=['ranking','movie_name', 'up&down'])
movie_table.to_csv("naver_movie.csv", encoding="cp949",mode='w', index=False)
print("end")
