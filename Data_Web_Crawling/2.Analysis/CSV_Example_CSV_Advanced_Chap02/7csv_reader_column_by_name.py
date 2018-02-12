"""열의 헤더를 사용하여 특정 열을 선택하는 방법-기본
- 열 헤더를 식별하기 쉽거나, 여러개의 입력 파일을 처리할때
- 열의 헤더는 같지만 열의 위치가 입력 파일에 따라 다를때
"""

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = ['Invoice Number', 'Purchase Date']
# 2개의 string value, 즉 2개의 column header
my_columns_index = []
# 2개의 관심 column의 value을 넣을 list
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
                # 각 column의 header가 my_columns에 있는 value 인지 판별
        filewriter.writerow(my_columns)
        for row_list in filereader:
            # my_columns_index 의 index 값을 반복하고 각 row의 data value를 가지고 온다
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)

"""
코드가 긴 이유는 선택하고자 하는 열 헤더의 index 값을 식별하려면 먼저 header행을 별도로
처리해야하기 때문이다.
그 다음 이러한 index 값을 사용하여 선택하려는 column의 header 와 동일한 index 값을 갖는
각 row의 data value를 추출할 수 있다.
"""