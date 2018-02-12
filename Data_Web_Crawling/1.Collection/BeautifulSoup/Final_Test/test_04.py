import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET


def div_file(count_number, dir_address):
    total_rows = int(len(nene_table))
    for i in range(total_rows):
        if i != 0:
            if i % count_number == 0:
                nene_table[(i - count_number):(i)].to_csv(dir_address + "nene%s.csv" % (i // count_number),
                                                          encoding="cp949", mode='w', index=True)
        else:
            continue
    nene_table[(total_rows // count_number) * count_number:].to_csv(
            dir_address + "nene%s.csv" % (total_rows // count_number + 1), encoding="cp949",
            mode='w', index=True)
    return None

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


dir_name = "V4_BigData"
dir_delimeter = "\\"
sdir_nene = "Nene_Data"
file_nene = "nene"
csv = ".csv"
dir_address = dir_name + dir_delimeter + sdir_nene + str() + dir_delimeter
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

if os.path.isfile(dir_name + dir_delimeter + "count.txt"):
    with open(dir_name + dir_delimeter + "count.txt", "r") as data:
        count_n = data.readline()
        count_n = int(count_n)
    os.mkdir(dir_name + dir_delimeter + sdir_nene + str(count_n))
    destination_folder = dir_name + dir_delimeter + sdir_nene + str(count_n) + dir_delimeter
    div_file(100, destination_folder)
    count_n += 1
    with open(dir_name + dir_delimeter + "count.txt", "w+") as data: data.write(str(count_n))

else:
    with open(dir_name + dir_delimeter+ "count.txt","w") as data: data.write("2")
    os.mkdir(dir_name + dir_delimeter + sdir_nene + "1")
    init_file = dir_name + dir_delimeter + sdir_nene + "1" + dir_delimeter
    div_file(100,init_file)
