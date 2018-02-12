"""CSV파일 읽고 쓰기(파트2)-기본"""

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
# 윈도우즈의 경우 csv 모듈에서 데이타를 쓸 때 각 라인 뒤에 빈 라인이 추가되는 문제가 있는데,
# 이를 없애기 위해 (파이썬 3 에서) 파일을 open 할 때 newline='' 와 같은 옵션을 지정
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter =',')
        # reader()함수를 이용해서 filereader 라는 input 파일을 읽는 객체를 만든다.
        filewriter = csv.writer(csv_out_file, delimiter =',')
        # write()함수를 이용해서 filewriter 라는 output 파일에 쓰는데 사용할 객체를 만든다.
        # delimiter =',' 기본값 인수, 입력 및 출력 파일이 쉼표로 구분되어있으면 안써도 됨
        for row_list in filereader:
            filewriter.writerow(row_list)
        # writerow function 를 사용하여 각 Row(행)의 value를 list 로 output_file에 쓴다
