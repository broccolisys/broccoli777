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

dir_name = "V2_BigData"
dir_delimeter = "\\"
sdir_nene = "Nene_Data"
file_nene = "nene"
csv = ".csv"
limit_n = 3

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

if os.path.isfile(dir_name + dir_delimeter + "count.txt"):
    with open(dir_name + dir_delimeter + "count.txt", "r") as data:
        count_n = data.readline()
        count_n = int(count_n)
        dir_n = int(count_n//limit_n)
        if count_n % limit_n != 0:
            dir_n += 1
        if count_n % limit_n == 1:
            os.mkdir(dir_name + dir_delimeter + sdir_nene + str(dir_n))

    destination_file = dir_name + dir_delimeter + sdir_nene + str(dir_n) + dir_delimeter + file_nene + str(count_n) + csv
    nene_table.to_csv(destination_file, encoding="cp949", mode='w', index=True)
    count_n += 1
    with open(dir_name + dir_delimeter + "count.txt", "w+") as data: data.write(str(count_n))

else:
    with open(dir_name + dir_delimeter+ "count.txt","w") as data: data.write("2")
    os.mkdir(dir_name + dir_delimeter + sdir_nene + "1")
    init_file = dir_name + dir_delimeter + sdir_nene + "1" + dir_delimeter + file_nene + "1" + csv
    nene_table.to_csv(init_file, encoding="cp949", mode='w', index=True)
