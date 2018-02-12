import csv
file_address = input("파일 위치와 이름, 확장명등을 입력하시오: " )
matters = ''
countParticipants = []

def get_csv_rowInstance(row_name):

    countParticipantsIndex = data[0].index(row_name)
    for row in data[1:]:
        countParticipants.append(row[countParticipantsIndex])
    return countParticipants

def print_row(row_Instance, type='int'):
    global matters
    for matter in row_Instance:
        matters += matter + "\n"
    print(matters)

def print_col(col_instance):
    data2 = list(csv.reader(infile))
    countParticipantsIndex2 = data2[col_instance]
    save_matter = ''
    for matter in countParticipantsIndex2:
        save_matter += matter + "\n"
    return save_matter

with open(file_address, newline='') as infile:
    print_row(get_csv_rowInstance("COUNT MALE"))
    print(print_col(0))




