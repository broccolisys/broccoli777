import csv
import math

class MathProgram:
    def __init__(self):
        self.


def check_type(self, header_index):
    self.header_index = header_index
    try :
        int_form =



with open('Demographic_Statistics_By_Zip_Code.csv', newline ='') as infile:
    data = list(csv.reader(infile))

while True:
    data_type = int(input("\n 원하는 서비스를 입력하세요.\n 1. 행 2. 열 3.총합 4.평균 "
                            "5. 최대값 6. 최소값 7. 편차 8. 표준편차 9. 분산 "
                            "10. 정렬(오름차,내림차) 11. 종료 \n: "))

    if data_type == 1:
        header_index = input("Header Index를 입력하세요: ")
        print("행 데이터는 아래와 같습니다.")
        print