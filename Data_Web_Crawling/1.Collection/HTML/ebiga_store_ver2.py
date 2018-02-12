import csv
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


def get_address_info():
    data_store = []
    for i in range(1, int(len(total_result))):
        address = total_result[i][2]
        data_store.append(address)
        i += 1
    return data_store

def get_canvas_info():
    canvas_store = []
    for canvas in get_address_info():
        canvas_data = canvas.split()
        canvas_store.append(canvas_data[0])
    canvas_str = str("/".join(canvas_store))
    canvas_str = canvas_str.replace('강서구','서울특별시')
    canvas_str = canvas_str.replace('서울특별시','서울')
    canvas_str = canvas_str.replace('서울시', '서울')
    canvas_str = canvas_str.replace('광주시', '광주')
    canvas_str = canvas_str.replace('전라남도','전남')
    canvas_str = canvas_str.replace('인천광역시','인천')
    canvas_str = canvas_str.replace('대구광역시','대구')
    canvas_str = canvas_str.replace('부산광역시','부산')
    canvas_str = canvas_str.replace('충청북도','충북')
    canvas_str = canvas_str.replace('충청남도','충남')
    canvas_str = canvas_str.replace('경기도','경기')
    canvas_str = canvas_str.replace('경상북도','경북')
    canvas_str = canvas_str.replace('경상남도','경남')
    canvas_str = canvas_str.replace('제주특별자치도', '제주')
    canvas_list = canvas_str.split("/")
    return canvas_list

def sum_data():
    sum_data = 0
    for city in set(get_canvas_info()):
        sum_data += int(get_canvas_info().count(city))
    return str(sum_data)


def record_cities():
    final_result = []
    for number in get_count():
        for city in set(get_canvas_info()):
            if number == get_canvas_info().count(city):
                result = [city] + [get_canvas_info().count(city)] + [int(get_canvas_info().count(city)*100)/int(sum_data())]
                final_result.append(result)
    return final_result

def record_cities_output():
    for number in get_count():
        for city in set(get_canvas_info()):
            if number == get_canvas_info().count(city):
                print("%36s" % city,"%3s" %" |","%5s"%get_canvas_info().count(city),"%5s" %" |","%5.4s" %((int(get_canvas_info().count(city)*100)/int(sum_data()))))

def get_count():
    count_store = []
    for city in set(get_canvas_info()):
        get_canvas_info().count(city)
        count_store.append(int(get_canvas_info().count(city)))
    count_store.sort(reverse=True)
    return count_store


print("\n%50s" % ("웹 스크롤링을 시작합니다"))
print("\n%50s" % ("Destination : "+ ebiga))
print("\n%53s" %("검색된 레코드 수 : "+ sum_data() + "개"))
print("\n%48s" % ("지역별 현황"))
print("\n%36s" %("지점"),"%3s" %"|","%5s"%"지점수","%3s" %"|","%3s"%"비율")
record_cities_output()

store_table = DataFrame(record_cities(), columns=('지점', '지점수',
                                               '비율'))
store_table.to_csv('Ebiga_store_BigData_가공정보(ver2).csv', encoding="cp949", mode='w', index=False)

