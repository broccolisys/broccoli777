import csv
import math
import random

def get_cvs_rowInstance(header_index):
    row_instance=[]
    row_index = data[0].index(header_index)
    for row in data[1:]:
        row_instance.append(row[row_index])
    return row_instance



def print_row(header_index):
    for row_element in check_type(header_index):
        print("%g" % row_element, end =" ")

with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as inflie:
    data = list(csv.reader(inflie))

while True:
    data_type =  int(input('\n'"원하는 서비스를 입력하세요. \n 1. 행 2.check \n: "))

    if data_type == 1:
        header_index = input("Header Column를 입력하세요: ")
        print("행 데이터는 아래와 같습니다.")
        print_row(header_index)
        continue

    elif data_type == 2:
        header_index = input("header_index 를 입력하세요: ")
        check_type(header_index)
        continue

    else:
        break