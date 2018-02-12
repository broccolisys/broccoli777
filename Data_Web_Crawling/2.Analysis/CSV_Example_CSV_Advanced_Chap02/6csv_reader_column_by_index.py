"""특정열(column) 선택하기-기본
1. column 의 index value를 사용하는 방법
2. column 의 header 를 사용하는 방법
"""
"""
열의 인덱스 값을 사용하여 특정 열을 선택하는 방법
- 열의 인덱스 값을 쉽게 식별할 수 있거나 여러개의 입력 파일을 처리할때
- 모든 입력 파일에서 열의 위치가 변경되지 않는 경우
"""
import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = [0,3]
# 선택하려는 두 column의 index value를 포함하는 my_columns 라는 list variable 생성
# 무조건 관심 index value 를 포함하는 variable를 만든다음 전체코드에서 그 변수를 참조하도록 하자

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
                # 관심 index 값에 해당하는 행의 값을 row_list_output에 저장한다
            filewriter.writerow(row_list_output)
