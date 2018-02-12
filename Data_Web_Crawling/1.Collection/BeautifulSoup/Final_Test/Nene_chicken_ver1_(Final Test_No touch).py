import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET
#  xml모듈을 가져오면서 xml.etree.ElementTree를 ET라는 새 이름으로 지정

result = []
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

# as ET가 없었다면 xml.etree.ElementTree.fromstring(..)으로 했었어야 했음. 그마저도 변수 xml때문에 문제가 생김

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

dir_name = "V1_BigData" # V1 큰 폴더 변수 지정
dir_delimeter = "\\" # 구분자 변수 지정
nene_dir = "Nene_Data" # 나중에 쓰일 소 폴더 변수 지정
nene_file = "nene" # 파일명 변수 지정
csv = ".csv" # 확장자 변수 지정

if not os.path.isdir(dir_name): # dir_name 해당하는 폴더가 없으면
    os.mkdir(dir_name) # dir_name 폴더를 만듬
if os.path.isfile(dir_name + dir_delimeter + "count.txt"): # count.txt 파일 존재 유무 확인
    with open(dir_name + dir_delimeter + "count.txt", 'r') as data:
        count_n = data.readline() # count.txt 첫번째줄 읽음
        count_n = int(count_n) # int 형 변환
        destination_file = dir_name + dir_delimeter + nene_file + str(count_n) + csv # 파일의 경로 및 이름, 확장자를 변수 지정함
        nene_table.to_csv(destination_file, encoding="cp949", mode='w', index=True) # 파일을 만듬
        count_n += 1 # count 하나 추가 후
    with open(dir_name + dir_delimeter + "count.txt", "w+") as data: data.write(str(count_n)) # 변경된 count 저장함
else: # count.txt. 파일 없을시
    with open(dir_name + dir_delimeter + "count.txt", 'w') as data: data.write("2") # w 모드로 count.txt 파일을 만들고, '2'(char) 로 만듬
    init_file = dir_name + dir_delimeter + nene_file + '1'+csv # 초기 파일 변수 지정
    nene_table.to_csv(init_file, encoding="cp949", mode='w', index=True) # nene1 파일(초기 파일)을 만듬
