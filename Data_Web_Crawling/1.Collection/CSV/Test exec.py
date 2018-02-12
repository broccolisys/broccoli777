import csv
import math
import random

class Sample():
    def __init__(self,header_index):
        self.header_index = header_index

    def get_csv_rowInstance(self):
        row_instance=[]
        row_index = data[0].index(self.header_index)
        for row in data[1:]:
            row_instance.append(float(row[row_index]))
        return row_instance

    def print_row(self):
        for row_element in Sample.get_csv_rowInstance(self.header_index):
            print("%g" % row_element, end =" ")


with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as inflie:
    data = list(csv.reader(inflie))

while True:
    data_type =  int(input('\n'"원하는 서비스를 입력하세요. \n 1. 행 2. 열 3.총합 4.평균 "
                            "5. 최대값 6. 최소값 7. 편차 8. 표준편차 9. 분산 "
                            "10. 정렬(오름차,내림차) 11. 종료 \n: "))

    if data_type == 1:
        header_index = input("Header Column를 입력하세요: ")
        print("행 데이터는 아래와 같습니다.")
        T6 = Sample(header_index)
        T6.print_row()

    else:
        break

