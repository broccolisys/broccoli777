"""2.10 여러 파일의 데이터 합치기-기본
유사한 데이터가 들어 있는 여러 개의 파일이 있는 경우 모든 데이터를 하나의 파일에 포함되도록
합쳐야 할때
"""
import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file: # 첫번째 입력 파일을 처리하고 헤더 행을 포함하여 모든 행을 출력 파일에 씀
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else: # 첫번째를 제외한 나머지 모든 입력 파일을 처리
                header = next(filereader) # 헤더행을 변수에 할당해서 포함시키지 않기 위해
                for row in filereader:
                    filewriter.writerow(row)