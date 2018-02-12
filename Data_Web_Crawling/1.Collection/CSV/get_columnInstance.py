import csv

def get_csv_columnInstance(primary_key):
    i = 0
    while True:
        if data[i][0] == str(primary_key):
            column_sentence = data[i]
            break
        else:
            i += 1
    column_instance = (" ".join([x for x in column_sentence]))
    print(column_instance)

def get_cvs_rowinstance(header_index):
    row_instance = []
    row_index = data[0].index(header_index)
    for row in data[1:]:
        row_instance.append(row[row_index])
    for row_element in row_instance:
        print(row_element)

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as inflie:
    data = list(csv.reader(inflie))

while True:
    data_type = int(input("Access 유형을 입력하세요(1.행, 2.열 3.종료) : "))
    if data_type == 1:
        header_index = input("Header Index를 입력하세요: ")
        print("행 데이터는 아래와 같습니다.")
        get_cvs_rowinstance(header_index)
        continue
    elif data_type == 2:
        primary_key = input("Access Key를 입력하세요: ")
        print("열 데이터는 아래와 같습니다.")
        get_csv_columnInstance(primary_key)
        continue

    else:
        break
