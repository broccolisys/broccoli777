"""2.9 여러개의 CSV 파일 읽기
파이썬의 내장된 glob 모듈을 통해 여러개의 csv 파일을 처리해보자
2.9.1 전체 파일 개수 및 각 파일의 행 및 열 개수 계산- 기본
행과 열의 개수를 세어보자
"""
import sys
import csv
import glob
import os

input_path = sys.argv[1]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    """glob 모듈은 특정 패턴과 일치하는 모든 경로명을 찾는다. 그리고 패턴은 정규표현식과 비슷하게 쓴다.
    "sales_*" 은 앞에 sales로 시작하는 이름을 가진 모든 파일을 경로안에서 찾는다. 만약 csv 파일을 모두
    처리하고 싶으면 *.csv 로 하면 된다(유닉스 셸 스타일의 와일드 카드 문자)
    os.path.join() function 을 통해 괄호 안에 있는 두개의 component 를 결합한다
    그리고 glob.glob() 함수는 sales_* 의 별표(*) 를 실제 파일명으로 확장한다.
    이것을 통해 glob.glob(os.path.join(input_path,'sales_*')) 는 세 개의 입력 파일이 있는 리스트를 만든다
    ['E:\workspace\Data_Web_Crawling\2.Analysis\CSV_Example_CSV_Advanced_Chap02\sales_february_2014.csv',
    ''E:\workspace\Data_Web_Crawling\2.Analysis\CSV_Example_CSV_Advanced_Chap02\sales_january_2014.csv',
    'E:\workspace\Data_Web_Crawling\2.Analysis\CSV_Example_CSV_Advanced_Chap02\sales_march_2014.csv']
    """

    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
    print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
        os.path.basename(input_file), row_counter, len(header)))
    # os.path.basename() 은 입력 받은 경로에서 파일명을 반환한다
    # 첫번째 값 :os.path.basename() function 을 이용하여 전체 경로명의 마지막 요소 추출
    # 두번째 값 : row_counter 변수를 사용하여 각 input_file 에서 행의 개수를 계산
    # 세번째 값 : len() 함수 이용하여, 각 input_file의 열 헤더가 들어있는 리스트 변수 header 에 들어있는 원소의 개수를 계산
    file_counter += 1
print('Number of files : {0:d}'.format(file_counter))

