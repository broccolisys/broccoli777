"""CSV파일 읽고 쓰기-기본"""

import sys # 명령 줄에서 추가적으로 입력된 인수(argv로부터)를 script로 넘겨줌

# argv는 cmd 에서 입력되는 인수를 리스트 자료형으로 받는다.
# Ordinary Env : python script_name.py "C:\path\to\input_file.csv" "C:\path\to\output_file.csv"
# Current Env : supplier_data.csv output_files\1output.csv

input_file = sys.argv[1]  # supplier_data.csv
output_file = sys.argv[2] # output_files\1output.csv

with open(input_file, 'r', newline='') as filereader: # input_file를 read
    with open (output_file, 'w', newline='') as filewriter : # output_file로 write
        header = filereader.readline() # file의 first_line를 string 형태로 읽고 그것을 header 변수 할당
        header = header.strip() # strip  함수를 이용해서 양끝 공백이나 개행문자 제거
        header_list = header.split(',') # ,를 기준으로 split에서 list로 저장한것이 header_list
        print(header_list) # print header_list
        filewriter.write(','.join(map(str,header_list))+'\n') # header_list 의 각 값을 filewriter 에 저장
        # map function : header_list의 가 원소에 str 함수를 적용하여 문자열로 만든다
        # join function : 각 값 사이에 ,(쉼표)를 삽입하고 list를 string로 변환한다
        # 다음 개행문자를 문자열 끝에 삽입
        # filewriter 객체는 그 문자열을 output_file의 첫번째 행에 기록한다

        for row in filereader: # header 를 제외한 나머지 행을 반복
            row = row.strip() # 양쪽 공백이나 개행문자 제거
            row_list = row.split(',') # , 를 기준으로 split 해서 list 로 저장
            print(row_list) # print로 확인
            filewriter.write(','.join(map(str,row_list))+'\n')
            # 위와 같은 단계로 filewriter 에 저장