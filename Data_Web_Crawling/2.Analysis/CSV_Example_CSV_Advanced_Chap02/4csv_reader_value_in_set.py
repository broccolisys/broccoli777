"""특정 집합의 값을 포함하는 행의 필터링-기본"""

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates = ['1/20/14', '1/30/14']
# 관심 값에 해당하는 두 날짜가 포함된 important_dates 라는 list variable를 만듬 - 관심 집합
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            # row_list[4] : Purchase Date column 을 가지고옴
            if a_date in important_dates:
            # 관심집합에 value와 a_date 의 value가 같으면 저장한다.
                filewriter.writerow(row_list)