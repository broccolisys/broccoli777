from bs4 import BeautifulSoup
from urllib.request import urlopen

max_pages = 10

result = []
index = "index"

for page_index in range(1, max_pages + 1)0:
    ebiga_adress = "http://www.ebiga.co.kr/home/bbs/board.php?bo_table=store")
    html
    html = urlopen(ebiga_adress)
    ebiga_html = BeautifulSoup(html, "html.parser")
    store_trs = ebiga_html.findAll('ul id', attrs='mobile_list')

    if (store_trs):
        for store_tr in store_trs:
            tr_tag = list(store_tr.strings)
            result.append(tr_tag)

print(result)