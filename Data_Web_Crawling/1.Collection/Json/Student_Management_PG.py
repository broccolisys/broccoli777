from collections import OrderedDict
import json
import os
import turtle

os_delimeter = "\\"
st_count = "Student_count_number.txt"
json_file_name = "ITT_Student.json"

def st_ID_Generator():
    try :
        with open(os.getcwd() + os_delimeter + st_count, "r") as data:
            count_n = data.readline()
            st_ID = "ITT" + count_n
            int_count_n = int("%01d" % int(count_n))
            int_count_n += 1
        with open(os.getcwd() + os_delimeter + st_count, "w") as count:
            three_digit_n = "%03d" % int_count_n
            count.write(three_digit_n)
            return st_ID
    except FileNotFoundError:
        with open(os.getcwd() + os_delimeter + st_count, "w") as file:
            file.write("002")
            st_initID = "ITT" + "001"
            return st_initID

def open_json_file():
    with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)
        return json_big_data

def fix_json_file():
    print("변경된 데이터를 저장 중입니다")
    with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
        readable_result = json.dumps(open_json_file(), indent=4, ensure_ascii=False)
        make_file.write(readable_result)
        print('저장이 완료되었습니다')


st_database = OrderedDict()
student_info = OrderedDict()
class_info = OrderedDict()
class_past_info = OrderedDict()
jsonData = OrderedDict()
lecture_info = OrderedDict()

while True:
    print("<<Json기반 주소록 관리 프로그램>>".center(50))
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료")
    pg_selection = int(input(":"))
    if pg_selection == 1: # 학생 ID는 ITT00X 순서대로 부여
        print("학생 정보 입력")
        st_name = str(input("이름 :"))
        student_info["이름"] = st_name
        st_old = str(input("나이 :"))
        student_info["나이"] = st_old
        st_address = str(input("주소 :"))
        student_info["주소"] = st_address
        print("수강 정보 입력")
        class_past_count = str(input("과거 수강 횟수 :"))
        class_info["과거수강횟수"] = class_past_count
        lecture_number = 1
        while True:
            class_code = str(input("강의 코드 :"))
            lecture_info["강의코드"] = class_code
            class_name = str(input("강의명 :"))
            lecture_info["강의명"] = class_name
            class_teacher = str(input("강사 :"))
            lecture_info["강사"] = class_teacher
            class_start = str(input("개강일 :"))
            lecture_info["개강일"] = class_start
            class_end = str(input("종료일 :"))
            lecture_info["종료일"] = class_end
            aggrement = int(input("강의를 추가하시겠습니까? 1/2"))
            if aggrement == 1:
                class_info["강좌"+str(lecture_number)] = lecture_info
                lecture_number+=1
                continue
            if aggrement == 2:
                class_info["강좌"+str(lecture_number)] = lecture_info
                break

        st_ID = st_ID_Generator()
        st_database["학생ID"] = st_ID
        st_database["학생정보"] = student_info
        st_database["수강정보"] = class_info
        jsonData = [st_database]

        try:
            with open(os.getcwd() + os_delimeter + json_file_name , encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                json_big_data = json.loads(json_string)
                total_json_data = json_big_data + jsonData
            with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
                readable_result = json.dumps(total_json_data, indent=4, ensure_ascii=False)
                make_file.write(readable_result)
                print('ITT_Student.json SAVED')
                continue

        except FileNotFoundError:
            with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
                readable_result = json.dumps(jsonData, indent=4, ensure_ascii=False)
                make_file.write(readable_result)
                print('ITT_Student.json SAVED')
                continue

    if pg_selection == 2: # 학생 정보 조회
        try:
            print("조회할 정보 선택(뒤로가기 0번): ")
            print("1.이름\t2.강의코드\t3.강의명\t4.강사\t5.뒤로가기")
            input_name = str(input("\n조회할 학생의 이름을 입력하시오(뒤로 가기 0번): "))
            for i in range(len(open_json_file() )):
                if input_name == (open_json_file() [i]["학생정보"]["이름"]):
                    print("조회된 학생 ID는 %s 입니다" % open_json_file() [i]["학생ID"])
                    print("1.전체 정보\n2.학생 정보\n3.수강 정보\n4.뒤로 가기")
                    info_num = int(input("원하시는 서비스를 선택 하세요: " ))
                    if info_num == 1:
                        print("학생ID: ",open_json_file() [i]["학생ID"])
                        for data1, data2 in (open_json_file()[i]["학생정보"].items()):
                            print(data1, ":", data2)
                        for data1, data2 in (open_json_file()[i]["과거수강횟수"].items()):
                            print(data1, ":", data2)
                        for data1, data2 in (open_json_file()[i]["수강정보"].items()):
                            print(data1, ":", data2)
                        continue
                    if info_num == 2:
                        for data1, data2 in (open_json_file()[i]["학생정보"].items()):
                            print(data1,":",data2)
                    if info_num == 3:
                        for data1, data2 in open_json_file()[i]["과거수강횟수"].items():
                            print(data1,":",data2)
                        for data1, data2 in open_json_file()[i]["수강정보"].items():
                            print(data1,":",data2)
                    if info_num == 4:
                        break
                if input_name == 0:
                    break

        except FileNotFoundError:
            print("파일이 없습니다")

    if pg_selection == 3: # 학생 정보 수정
        with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
        print("수정하실 학생의 ID나 이름을 입력하시오(뒤로가기 0번):")
        input_value = str(input(":"))
        if input_value == 0:
            break
        else:
            for i in range(len(json_big_data)):
                if input_value == (json_big_data[i]["학생정보"]["이름"]) or input_value == (json_big_data[i]["학생ID"]):
                    while True:
                        print("수정하실 항목을 선택하시오")
                        fix_number = int(input("1.학생 정보\n2.수강 정보\n3.뒤로 가기:"))
                        if fix_number == 1:
                            while True:
                                print("수정하실 학생 정보를 선택하시오")
                                print("1.이름\n2.나이\n3.주소\n4.뒤로가기")
                                st_fix_num = int(input(":"))
                                if st_fix_num == 1:
                                    print("이름을 선택하셨습니다")
                                    print("현재 이름은",(json_big_data[i]["학생정보"]["이름"]),"입니다" )
                                    input_name = str(input("수정할 원하는 이름을 입력하시오\n:"))
                                    (json_big_data[i]["학생정보"]["이름"])=input_name
                                    print((json_big_data[i]["학생정보"]["이름"]),"로 수정되었습니다")
                                    continue
                                if st_fix_num == 2:
                                    print("나이를 선택하셨습니다")
                                    print("현재 나이는", (json_big_data[i]["학생정보"]["나이"]), "입니다")
                                    input_old = str(input("수정할 원하는 나이를 입력하시오\n:"))
                                    (json_big_data[i]["학생정보"]["나이"]) = input_old
                                    print((json_big_data[i]["학생정보"]["나이"]), "로 수정되었습니다")
                                    continue
                                if st_fix_num == 3:
                                    print("주소를 선택하셨습니다")
                                    print("현재 주소는", (json_big_data[i]["학생정보"]["주소"]), "입니다")
                                    input_address = str(input("수정할 원하는 주소를 입력하시오\n:"))
                                    (json_big_data[i]["학생정보"]["주소"]) = input_address
                                    print((json_big_data[i]["학생정보"]["주소"]), "로 수정되었습니다")
                                    continue
                                if st_fix_num == 4:
                                    print("변경된 사항을 저장하겠습니다")
                                    with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
                                        readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
                                        make_file.write(readable_result)
                                        print('저장되었습니다')
                                        break

                        if fix_number == 2:
                            while True:
                                print("수정하실 수강 정보를 선택하시오")
                                print("1.과거 수강 횟수\n2.강의 코드\n3.강의명\n4.강사\n5.개강일\n6.종료일\n7.뒤로가기")
                                ins_fix_num = int(input(":"))
                                if ins_fix_num == 1:
                                    print("과거 수강 횟수를 선택하셨습니다")
                                    print("현재 과거 수강 횟수는", (json_big_data[i]["과거수강횟수"]["과거수강횟수"]), "입니다")
                                    input_name = str(input("수정할 원하는 과거 수강 횟수를 입력하시오\n:"))
                                    (json_big_data[i]["과거수강횟수"]["과거수강횟수"]) = input_name
                                    print((json_big_data[i]["과거수강횟수"]["과거수강횟수"]), "로 수정되었습니다")
                                    continue
                                if ins_fix_num == 2:
                                    print("강의코드를 선택하셨습니다")
                                    print("현재 강의코드는", (json_big_data[i]["수강정보"]["강의코드"]), "입니다")
                                    input_name = str(input("수정할 원하는 강의 코드를 입력하시오\n:"))
                                    (json_big_data[i]["수강정보"]["강의코드"]) = input_name
                                    print((json_big_data[i]["수강정보"]["강의코드"]), "로 수정되었습니다")
                                    continue
                                if ins_fix_num == 3:
                                    print("강의명를 선택하셨습니다")
                                    print("현재 강의명은", (json_big_data[i]["수강정보"]["강의명"]), "입니다")
                                    input_name = str(input("수정할 원하는 강의 코드를 입력하시오\n:"))
                                    (json_big_data[i]["수강정보"]["강의명"]) = input_name
                                    print((json_big_data[i]["수강정보"]["강의명"]), "로 수정되었습니다")
                                    continue
                                if ins_fix_num == 4:
                                    print("강사를 선택하셨습니다")
                                    print("현재 강사는", (json_big_data[i]["수강정보"]["강사"]), "입니다")
                                    input_name = str(input("수정할 원하는 강사를 입력하시오\n:"))
                                    (json_big_data[i]["수강정보"]["강사"]) = input_name
                                    print((json_big_data[i]["수강정보"]["강사"]), "로 수정되었습니다")
                                    continue
                                if ins_fix_num == 5:
                                    print("개강일를 선택하셨습니다")
                                    print("현재 개강일은", (json_big_data[i]["수강정보"]["개강일"]), "입니다")
                                    input_name = str(input("수정할 원하는 개강일을 입력하시오\n:"))
                                    (json_big_data[i]["수강정보"]["개강일"]) = input_name
                                    print((json_big_data[i]["수강정보"]["개강일"]), "로 수정되었습니다")
                                    continue
                                if ins_fix_num == 6:
                                    print("종료일를 선택하셨습니다")
                                    print("현재 종료일은", (json_big_data[i]["수강정보"]["종료일"]), "입니다")
                                    input_name = str(input("수정할 원하는 종료일을 입력하시오\n:"))
                                    (json_big_data[i]["수강정보"]["종료일"]) = input_name
                                    print((json_big_data[i]["수강정보"]["종료일"]), "로 수정되었습니다")
                                    continue
                                if ins_fix_num == 7:
                                    print("변경된 사항을 저장하겠습니다")
                                    with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
                                        readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
                                        make_file.write(readable_result)
                                        print('저장되었습니다.')
                                        break
                        if fix_number == 3:
                            break

    if pg_selection == 4: # 학생 정보 삭제
        with open(os.getcwd() + os_delimeter + json_file_name, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            json_big_data = json.loads(json_string)
        print("삭제할 학생의 ID를 입력하시오(뒤로가기 0번):")
        input_value = str(input(":"))
        if input_value == 0:
            break
        else:
            for i in range(len(json_big_data)):
                if input_value == (json_big_data[i]["학생ID"]):
                    while True:
                        print("삭제할 항목을 선택하시오")
                        print("1. 전체 항목\n 2.수강 정보\n3.뒤로가기")
                        del_number = int(input(":"))
                        if del_number == 1:
                            agreement = str(input("전체 항목을 삭제하시겠습니까? Y/N"))
                            if agreement == "Y":
                                del(json_big_data[i])
                                print("전체 항목을 삭제하였습니다")
                            if agreement == "N":
                                print("취소하였습니다")
                                break
                        if del_number == 2:
                            agreement = str(input("수강 정보를 삭제하시겠습니까? Y/N"))
                            if agreement == "Y":
                                del(json_big_data[i]["수강정보"])
                                print("수강 정보를 삭제하였습니다")
                            if agreement == "N":
                                print("취소하였습니다")
                                break
                        if del_number == 3:
                            print("변경된 사항을 저장하겠습니다")
                            with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
                                readable_result = json.dumps(json_big_data, indent=4, ensure_ascii=False)
                                make_file.write(readable_result)
                                print('저장되었습니다.')
                                break

    if pg_selection == 5: # 프로그램 종료
        break

    else:
        print("잘못 입력하셨습니다")
    #
    #     with open(os.getcwd() + os_delimeter +'ITT_Student.json', 'w', encoding='utf8') as outfile:
    #         readable_result = json.dumps(st_datebase, indent=4, sort_keys=True, ensure_ascii=False)
    #         outfile.write(readable_result)
    #         print('ITT_Student.json SAVED')
    #         break