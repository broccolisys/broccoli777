import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET

record_limit = 3
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

if os.path.isdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\"):
    if os.path.isfile("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt"):
        count_number = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt", 'r')
        count = str(count_number.readline())
        count_number.close()
        count = int(count)
        value_chdir = count // (record_limit+1)
        if value_chdir == 0:
            try:
                os.mkdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_1")
                os.chdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_1")
                nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
                count = int(count) + 1
                count = str(count)
                count_number_new = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt", 'w')
                count_number_new.write(count)
                count_number_new.close()
            except FileExistsError:
                os.chdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_1")
                nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
                count = int(count) + 1
                count = str(count)
                count_number_new = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt", 'w')
                count_number_new.write(count)
                count_number_new.close()
        else:
            if count % (record_limit+1) == 0:
                os.mkdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_"+str(value_chdir+1))
                os.chdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_"+str(value_chdir+1) )
                nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
                count = int(count) + 1
                count = str(count)
                count_number_new = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt", 'w')
                count_number_new.write(count)
                count_number_new.close()
            else:
                os.chdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_" +str(value_chdir+1))
                nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
                count = int(count) + 1
                count = str(count)
                count_number_new = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt", 'w')
                count_number_new.write(count)
                count_number_new.close()

else:
    os.mkdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\")
    make_count = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt",'a')
    data = '1'
    make_count.write(data)
    make_count.close()
    count_number = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt", 'r')
    count = str(count_number.readline())
    count_number.close()
    count = int(count)
    value_chdir = count // (record_limit + 1)
    os.mkdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_1")
    os.chdir("E:\workspace\Python\Jumptopy\XML\V2_BigData\\Nene_Data_1")
    nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
    count = int(count) + 1
    count = str(count)
    count_number_new = open("E:\workspace\Python\Jumptopy\XML\V2_BigData\\count.txt", 'w')
    count_number_new.write(count)
    count_number_new.close()
