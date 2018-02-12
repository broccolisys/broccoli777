from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html.read(), "html.parser")
print(bs0bj.h1)