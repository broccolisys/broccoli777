import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

URL = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')
l = soup.find_all("tbody")
print(l)
movie_table = DataFrame(l)
movie_table.to_csv("test_movie.csv", encoding="cp949",mode='w', index=True)
print("end")
