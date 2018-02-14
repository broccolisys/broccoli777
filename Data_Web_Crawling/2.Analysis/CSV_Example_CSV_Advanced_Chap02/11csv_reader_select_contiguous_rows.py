"""연속된 행 선택하기-기본
입력 파일에 불필요한 머리말과 꼬리말 정보가 있을때 연속된 행 선택하기로
필요한 정보를 가지고 와보자
특정한 행을 선택하기 위해 row_counter 라는 variable 변수를 추가하자
이 변수를 통해서 row를 추적하여 포함할 row를 식별하고 선택할 수 있다.
"""

import csv
import sys

input_file = sys.argv[1]
output_file =sys.argv[2]

row_counter = 0
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file, 'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
            # if 문을 통해 row_counter 변수를 사용하여 원하는 행만 선택하고 원하지 않는 헤더 및 푸터 내용은 건너뛴다
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1
