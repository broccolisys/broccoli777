import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET

result = []
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

result = []
dir_name = "V4_BigData"
dir_delimiter = "\\"
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"
record_limit = 3

def make_dir(index) :
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(index))
    return None

def make_hundred(dir_index, file_index): #100을 넣어줘야함
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + nene_file + str(file_index) + csv
    total_rows = int(len(nene_table))
    count_number = 100
    for i in range(total_rows):
        if i != 0:
            if i % 100 == 0:
                nene_table[(i - count_number):(i)].to_csv(destination_csv, encoding="cp949",mode='w', index=True)
        else:
            continue
    nene_table[(total_rows // count_number) * count_number:].to_csv(destination_csv,encoding="cp949", mode='w', index=True)
    return None

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

try :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'r') as file :
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index / record_limit)
        if file_index % record_limit != 0 :
            dir_index = dir_index+1
        if file_index % record_limit == 1 :
            make_dir(dir_index)

        make_hundred(dir_index, file_index)
        file_index += 1
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write(str(file_index))
except FileNotFoundError :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write('2')
    make_dir(1)
    make_hundred(1, 1)
print("End")