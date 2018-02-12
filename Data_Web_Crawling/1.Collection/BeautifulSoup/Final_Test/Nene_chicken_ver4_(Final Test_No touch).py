import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET
import time

def div_file(count_number,dir_adress):
    total_rows = int(len(nene_table))
    for i in range(total_rows):
        if i != 0:
            if i % count_number == 0:
                nene_table[(i - count_number):(i)].to_csv(dir_adress+ 'nene%s.csv' % (i // count_number),
                                                          encoding="cp949",
                                                          mode='w', index=True)
        else:
            continue

    nene_table[(total_rows // count_number) * count_number:].to_csv(dir_adress+ 'nene%s.csv' % (total_rows // count_number + 1),
                                                                    encoding="cp949", mode='w', index=True)
    return None

result = []
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체'))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

now = time.localtime()
now_time = "%04d-%02d-%02d-%02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

result = []
dir_name = "V4_BigData"
dir_delimeter = "\\"
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"

if not os.path.isdir(dir_name): # dir_name 해당하는 폴더가 없으면
    os.mkdir(dir_name) # dir_name 폴더를 만듬
if os.path.isfile(dir_name + dir_delimeter + "count.txt"): # count.txt 파일 존재 유무 확인
    with open(dir_name + dir_delimeter + "count.txt", 'r') as data:
        count_n = data.readline() # count.txt 첫번째줄 읽음
        count_n = int(count_n) # int 형 변환
        destination_folder = dir_name + dir_delimeter + nene_dir + str(count_n) + dir_delimeter
        os.mkdir(destination_folder)  # Nene_Data 폴더를 만듬
        div_file(100, destination_folder)
        count_n += 1  # count 하나 추가
        with open(dir_name + dir_delimeter + "count.txt", "w+") as data: data.write(str(count_n)) # 변경된 count 추가함

else: # count.txt. 파일 없을시
    with open(dir_name + dir_delimeter + "count.txt", 'w') as data: data.write("2") # w 모드로 count.txt 파일을 만들고, '2'(char) 로 만듬
    init_nene_dir = dir_name + dir_delimeter + nene_dir + "1" + dir_delimeter # 처음 Nene_Data1 폴더 변수 지정
    os.mkdir(init_nene_dir) # Nene_Data1 폴더를 만듬
    div_file(100,init_nene_dir)