from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame

max_pages = 10
result_1 = []
result_2 = []
result_3 = []
total_result = []

ebiga = 'http://www.ebiga.co.kr/home/bbs/board.php?bo_table=store&page=%s'
for page_idx in range(1,max_pages+1):
    ebiga_URL= 'http://www.ebiga.co.kr/home/bbs/board.php?bo_table=store&page=%s'% str(page_idx)
    response = urlopen(ebiga_URL)
    soupData = BeautifulSoup(response.read(),'html.parser')
    store_name =soupData.findAll('div',attrs={'class':'subject'})
    store_address = soupData.findAll('div',attrs={'class':'address'})
    store_phone = soupData.findAll('div',attrs={'class':'phone'})
    # print(store_phone)

    if(store_name):
        for store_tr in store_name:
            store_tag = list(store_tr.strings)
            store_name_tag = store_tag[0]
            result_1.append([store_name_tag])

    if(store_address):
        for store_adtr in store_address:
            store_adtag = list(store_adtr.strings)
            store_address_tag = store_adtag[0]
            result_2.append([store_address_tag])

    if(store_phone):
        for store_phtr in store_phone:
            store_phtag = list(store_phtr.strings)
            store_phone_tag = store_phtag[0]
            result_3.append([store_phone_tag])

for i in range(int(len(result_1))):
    if i == 0:
        total_ebiga = [1] + result_1[i] + result_2[i] + result_3[i]
        total_result.append(total_ebiga)
    else:
        total_ebiga = [i+1] + result_1[i] + result_2[i] + result_3[i]
        total_result.append(total_ebiga)

print("\n%50s" % ("웹 스크롤링을 시작합니다"))
print("\n%50s" % ("Destination : "+ ebiga))
print("\n%46s" % ("지역별 현황"))
print("\n%24s" %("전화번호"),"%4s" %"|","%12s"%"지점명","%32s"%"주소")
for i in range(int(len(total_result))):
    print("%27s" %(total_result[i][3]),"%4s" %"|", total_result[i][1].center(20), total_result[i][2].center(31))

store_table = DataFrame(record_cities(), columns=('전화번호', '지점명', '주소'))
store_table.to_csv('Ebiga_store_BigData_가공정보(ver1).csv', encoding="cp949", mode='w', index=False)
