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

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

if os.path.isdir("E:\workspace\Python\Jumptopy\XML\V4_BigData\\"):
    os.chdir("E:\workspace\Python\Jumptopy\XML\V4_BigData\\")
    count_number = open("E:\workspace\Python\Jumptopy\XML\V4_BigData\\count.txt", 'r')
    count = str(count_number.readline())
    count_number.close()
    count = int(count)
    os.mkdir("E:\workspace\Python\Jumptopy\XML\V4_BigData\\Nene_Data_%s" % count)
    os.chdir("E:\workspace\Python\Jumptopy\XML\V4_BigData\\Nene_Data_%s" % count)
    total_rows = int(len(nene_table))
    count_number = 100
    for i in range(total_rows):
        if i != 0:
            if i % 100 == 0:
                nene_table[(i - count_number):(i)].to_csv('nene%s.csv' % (i // count_number), encoding="cp949",
                                                          mode='w', index=True)
        else:
            continue
    nene_table[(total_rows // count_number) * count_number:].to_csv('nene%s.csv' % (total_rows // count_number + 1),
                                                                    encoding="cp949", mode='w', index=True)
    count = int(count) + 1
    count = str(count)
    count_number_new = open("E:\workspace\Python\Jumptopy\XML\V4_BigData\\count.txt", 'w')
    count_number_new.write(count)
    count_number_new.close()

else:
    os.mkdir(dir_name + dir_delimiter + nene_dir + str('1'))
    os.chdir(dir_name + dir_delimiter + nene_dir + str('1'))
    with open(dir_name + dir_delimiter + "count.txt", 'w') as data:
        data.write('2')
    total_rows = int(len(nene_table))
    count_number = 100
    for i in range(total_rows):
        if i != 0:
            if i % 100 == 0:
                nene_table[(i - count_number):(i)].to_csv('nene%s.csv' % (i // count_number), encoding="cp949", mode='w',                                               index=True)
        else:
            continue
    nene_table[(total_rows // count_number) * count_number:].to_csv('nene%s.csv' % (total_rows // count_number + 1),encoding="cp949", mode='w', index=True)


