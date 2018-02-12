import urllib.request
from pandas import DataFrame
import os

def div_file(count_n, dir_address): # count_n = 끊을 개수 단위, dir_address = 저장할 위치, 파일을 100개씩 묶을 함수 만들어줌
    total_rows = int(len(nene_table)) # nene_table 의 총 개수를 가지고 온다
    for i in range(total_rows): # for 문을 돌려
        if i != 0: # i 가 0일 경우 파일이름이 0이 시작되므로 피한다
            if i % count_n == 0: # count_n 이 100이라면 i는 100,200,300,400,,,,1100까지 뽑아진다.
                nene_table[(i-count_n):(i)].to_csv(dir_address + "nene%s.csv" % (i//count_n), encoding="cp949", mode='w', index=True)
                # Splicing 을 이용해서 100개의 파일을 뽑는다. 파일명의 숫자는 i와 count_n의 몫을 이용한다
        else:
            continue
    nene_table[(total_rows//count_n)*count_n:].to_csv(dir_address + "nene%s.csv" % ((total_rows // count_n) + 1), encoding="cp949", mode='w',index=True)
    # 1100 번 파일 이후의 남은 파일 또한 뽑는다.
    return None

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

dir_name = "V4_Bigdata" # 큰 폴더 변수 지정
dir_delimeter = "\\" # 구분자 변수 지정
sdir_nene = "Nene_data" # 소 폴더 변수 지정
file_name = "nene" # 파일 이름 변수 지정
csv = ".csv" # 확장자 변수 지정

if not os.path.isdir(dir_name): # dir_name 폴더 유무
    os.mkdir(dir_name) # 없으면 dir_name 폴더를 만들어 준다

if os.path.isfile(dir_name + dir_delimeter + "count.txt"): # count 파일 유무
    with open(dir_name + dir_delimeter + "count.txt", "r") as data: #  count 파일 읽음
        count_n = data.readline() # 첫번째 라인 읽음
        count_n = int(count_n) # 첫번째 라인 정수형 변환
    destination_folder = dir_name + dir_delimeter + sdir_nene + str(count_n) + dir_delimeter # 만들어질 폴더 경로 변수 지정
    os.mkdir(destination_folder) # 소폴더 생성
    div_file(100, destination_folder) # 함수 이용해서 파일을 뽑아냄
    count_n += 1 # 카운터 1 증가
    with open(dir_name + dir_delimeter +"count.txt", "w+") as data: # 증가된 카운터 저장
        data.write(str(count_n))

else:
    with open(dir_name + dir_delimeter + "count.txt", "w") as data: data.write("2") # count.txt 생성, 초기값 "2"
    os.mkdir(dir_name + dir_delimeter + sdir_nene + "1" ) #  소폴더 Nene_data1 생성
    init_folder = dir_name + dir_delimeter + sdir_nene + "1" + dir_delimeter # 경로 변수 저장
    div_file(100, init_folder) # 함수 이용해서 초기 csv 데이터 뽑아냄

