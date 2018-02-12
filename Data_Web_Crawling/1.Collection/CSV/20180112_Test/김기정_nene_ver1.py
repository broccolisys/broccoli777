import urllib.request
from pandas import DataFrame
import os
result = []

import xml.etree.ElementTree as ET
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))

dir_name = "V1_Bigdata" # 큰 폴더 변수 지정
dir_delimeter = "\\" # 구분자 변수 지정
sdir_nene = "Nene_data" # 소 폴더 변수 지정(ver2 부터 사용)
file_name = "nene" # 파일 이름 변수 지정
csv = ".csv" # 확장자 변수 지정

if not os.path.isdir(dir_name): # dir_name 폴더 유무
    os.mkdir(dir_name) # 없으면 dir_name 폴더를 만들어 준다

if os.path.isfile(dir_name + dir_delimeter + "count.txt"): # count.txt 파일 유무
    with open(dir_name + dir_delimeter + "count.txt", "r") as data: #  count.txt 파일 읽음
        count_n = data.readline() # 첫번째 라인 읽음
        count_n = int(count_n) # 첫번째 라인 정수형 변환
    destination_file = dir_name + dir_delimeter + file_name + str(count_n) + csv # 만들어질 파일 경로 변수 지정
    nene_table.to_csv(destination_file, encoding="cp949", mode='w', index=True)  # 파일 생성
    count_n += 1 # 카운터 1 증가
    with open(dir_name + dir_delimeter +"count.txt", "w+") as data: # 증가된 카운터 저장
        data.write(str(count_n))

else:
    with open(dir_name + dir_delimeter + "count.txt", "w") as data: data.write("2") # count.txt 생성, 초기값 "2"
    init_file = dir_name + dir_delimeter + file_name + "1" + csv # 처음 만들 파일 경로 변수 지정
    nene_table.to_csv(init_file, encoding="cp949", mode='w', index=True) # 처음 파일 생성
