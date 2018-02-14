"""2.8 헤더 추가하기-기본
가끔씩 헤더 행이 포함되지 않는 경우가 종종 있다. 이럴때 파이썬 스크립트를 이용해 열 헤더를 추가할 수 있다.
"""

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number',\
                       'Part Number', 'Cost', 'Purchase Date']
        filewriter.writerow(header_list)
        # header_list 를 다 쓰고
        for row in filereader:
            filewriter.writerow(row)
        # 나머지 데이터를 쓴다
