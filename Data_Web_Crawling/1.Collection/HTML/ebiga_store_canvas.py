from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame

max_pages = 2
result_1 = []
result_2 = []
result_3 = []
total_result = []


for page_idx in range(1,max_pages+1):
    ebiga_URL= 'http://www.ebiga.co.kr/home/bbs/board.php?bo_table=store&sca=%s'% str(page_idx)
    response = urlopen(ebiga_URL)
    soupData = BeautifulSoup(response.read(),'html.parser')
    store_name =soupData.findAll('div',attrs={'class':'subject'})
    store_address = soupData.findAll('div',attrs={'class':'address'})
    store_phone = soupData.findAll('div',attrs={'class':'phone'})
    print(store_name)