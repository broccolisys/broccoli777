from collections import OrderedDict
import os
import json

now_cwd = os.getcwd()
file_delimeter = "\\"
count_file = "student_count_file.txt"
json_file = "ITT_Student.json"
json_default = []
main_dict = OrderedDict()
class_dict = OrderedDict()

def main_interface():
    print("<<Json기반 주소록 관리 프로그램>>")
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료")

def register_interface():
    print("수정하실 학생 정보를 선택하시오")
    print("1. 이름")
    print("2. 나이")
    print("3. 주소")
    print("4. 과거수강횟수")
    print("5. 강의코드")
    print("6. 강의명")
    print("7. 강사")
    print("8. 뒤로가기")

def json_file_check():
    if os.path.isfile(json_file):
        print("로딩되었습니다")
    else:
        print("기본 경로에 파일이 없습니다")
        print("1.기본 경로 신규 생성")
        print("2.파일 경로 입력")
        where_file = int(input(">>"))
        if where_file == 1:
            json_file_save(json_default, now_cwd + file_delimeter)
        elif where_file == 2:
            try:
                json_file_address = str(input("json 파일 경로를 입력하시오\n>>"))
                json_file_load(json_address_from_input(json_file_address))
                print("파일 로딩 완료")
            except FileNotFoundError:
                print("입력하신 경로에 파일이 없습니다. 기본 경로에 새로 생성합니다")
                json_file_save(json_default,now_cwd+file_delimeter)
        else:
            print("잘못입력하셨습니다")

def json_address_from_input(address):
    json_file_address = address + file_delimeter
    os.chdir(json_file_address)
    return json_file_address

def json_file_save(content,address):
    with open(address + file_delimeter + "ITT_Student.json", 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(content, indent=4, ensure_ascii=False)
        outfile.write(readable_result)
        print('ITT_Student.json SAVED')

def json_file_load(address):
    with open(address + file_delimeter + "ITT_Student.json", encoding='UTF8') as json_file: json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)
    return json_big_data

def count_file_check():
    if not os.path.isfile(now_cwd + file_delimeter + count_file):
        with open(now_cwd + file_delimeter + count_file, "w") as count:
            count.write("001")

def count_file_load():
    with open(now_cwd + file_delimeter + count_file, "r") as count:
        count_readline = count.readline()
        student_id = "ITT" + count_readline
        count_int = int("%01d" % int(count_readline))
        count_int += 1
    with open(now_cwd + file_delimeter + count_file, "w") as fix_count:
        count_three_digit = str("%03d" % count_int)
        fix_count.write(count_three_digit)
        return student_id

def student_register():
    st_name = str(input("이름\nex)김기정\n>>"))
    st_old = str(input("나이\nex)20\n>>"))
    st_address = str(input("주소\nex)대구시\n>>"))
    return [st_name, st_old, st_address]

def past_register():
    class_past_count = str(input("과거수강횟수\nex)5\n>>"))
    return class_past_count

def class_register():
    class_code = str(input("강의 코드\nex)BIT3322\n>>"))
    class_name = str(input("강의명\nex)인공지능\n>>"))
    class_teacher = str(input("강사\nex)김팔봉\n>>"))
    class_start = str(input("개강일\nex)20180101\n>>"))
    class_end = str(input("종료일\nex)20190101\n>>"))
    return [class_code, class_name, class_teacher, class_start, class_end]

def student_info():
    import_data = student_register()
    personnel_info = dict(zip(["이름","나이","주소"],import_data))
    return personnel_info

def past_info():
    import_data = past_register()
    return import_data

def class_info():
    import_data = class_register()
    class_info = dict(zip(["강의코드","강의명","강사","개강일","종료일"],import_data))
    return class_info

json_file_check()
count_file_check()

while True:
    main_interface()
    category_select = int(input("항목 선택\n>>"))
    if category_select == 1:
        print("학생 등록 프로그램 실행")
        register_interface()
        print("등록하실 정보를 입력하시오")
        main_dict["학생ID"] = count_file_load()
        main_dict["학생정보"] = student_info()
        class_dict["과거수강횟수"] = past_info()
        count = 1
        class_dict["강좌" + str(1)] = class_info()
        while True:
            class_number = int(input("추가하실려면 1, 취소하실려면 2\n>>"))
            if class_number == 1:
                class_dict["강좌" + str(count+1)] = class_info()
                count += 1
                break
            if class_number == 2:
                break

        main_dict["수강정보"] = class_dict
        total_json_data = json_file_load(os.getcwd()) + [main_dict]
        print(total_json_data)
        json_file_save(total_json_data,os.getcwd())
        print("완료")
    # elif ctegory_select == 2:
    # elif category_select == 3:
    # elif category_select == 4:
    # elif category_select == 5:
    else:
        print("잘못입력하셨습니다")
