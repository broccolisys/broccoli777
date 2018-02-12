import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET

result = []
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
# response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)


for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

dir_name = "V1_BigData"
dir_delimeter = "\\"
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

if os.path.isfile(dir_name + dir_delimeter + "count.txt"):
    with open(dir_name + dir_delimeter + "count.txt", "r") as data:
        count_n = data.readline()
        count_n = int(count_n)
    destination_file = dir_name + dir_delimeter + nene_file + str(count_n) + csv
    nene_table.to_csv(destination_file,  encoding="cp949", mode='w', index=True)
    count_n += 1
    with open(dir_name + dir_delimeter + "count.txt", "w+") as data:
        data.write(str(count_n))

else:
    with open(dir_name + dir_delimeter + "count.txt", "w") as data: data.write('2')
    init_file = dir_name + dir_delimeter + nene_file+ "1" + csv
    nene_table.to_csv(init_file, encoding="cp949", mode='w', index=True)