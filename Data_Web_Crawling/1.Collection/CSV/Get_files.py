def print_col(col_instance):
    try:
        import csv
        with open(file_address, newline='') as infile2:
            data2 = list(csv.reader(infile2))
            countParticipantsIndex2 = data2[col_instance]
            # matters = ''
            for matter in countParticipantsIndex2:
                print(matter)
            #     matters += matter + '\n'
            # return matters
    except FileNotFoundError as e:
        print("잘못된 파일 위치이거나 파일을 찾을수 없습니다.")
    except ValueError as e:
        print("관련된 열 값(Col Instance)을 찾을수 없습니다")

file_address = input("파일 위치와 이름, 확장명등을 입력하시오: " )
col_instance = int(input(" : "))
print_col(2)