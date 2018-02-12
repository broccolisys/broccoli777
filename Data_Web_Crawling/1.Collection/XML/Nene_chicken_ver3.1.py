import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET
import time

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
dir_name = "V2_BigData"
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"
record_limit = 3

now = time.localtime()
now_time = "%04d-%02d-%02d-%02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

try:
    with open(dir_name + "\\"+ "count.txt", 'r') as file:
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index / record_limit)
        if file_index % record_limit != 0 :
            dir_index = dir_index+1
        if file_index % record_limit == 1 :
            os.mkdir(dir_name + "\\" + nene_dir + str(dir_index))

        destination_csv = dir_name + "\\" + nene_dir + str(dir_index) + "\\" + nene_file + str(file_index) +now_time + csv
        nene_table.to_csv(destination_csv, encoding="cp949", mode='w', index=True)
        file_index += 1

    with open(dir_name + "\\"+ "count.txt", 'w') as file:
        file.write(str(file_index))

except FileNotFoundError:
    with open(dir_name + "\\" + "count.txt", 'w') as file:
        file.write('2')
    os.mkdir(dir_name + '\\' + nene_dir + str(1))
    destination_csv = dir_name + "\\"+ nene_dir + str(1) + "\\" + nene_file + str(1) + now_time + csv
    nene_table.to_csv(destination_csv, encoding="cp949", mode='w', index=True)

print("End")