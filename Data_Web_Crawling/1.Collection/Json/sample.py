t = [
    {
        "학생ID": "ITT001",
        "학생정보": {
            "이름": "김기정",
            "나이": "31",
            "주소": "대구시"
        },
        "수강정보": {
            "과거수강횟수": "1",
            "강좌0": {
                "강의코드": "ITITIT333",
                "강의명": "호라이",
                "강사": "오오",
                "개강일": "2019",
                "종료일": "29129"
            },
            "강좌1": {
                "강의코드": "SKSKSID",
                "강의명": "모자",
                "강사": "호랑아아아",
                "개강일": "3939",
                "종료일": "229"
            }
        }
    },{
        "학생ID": "ITT002",
        "학생정보": {
            "이름": "김기정",
            "나이": "32",
            "주소": "대구시"
        },
        "수강정보": {
            "과거수강횟수": "1",
            "강좌0": {
                "강의코드": "ITITIT333",
                "강의명": "호라이",
                "강사": "오오",
                "개강일": "2019",
                "종료일": "29129"
            },
            "강좌1": {
                "강의코드": "SKSKSID",
                "강의명": "모자",
                "강사": "호랑아아아",
                "개강일": "3939",
                "종료일": "229"
            }
        }
    }
]

from collections import OrderedDict
import json
import os
import sys

os_delimeter = "\\"
st_count = "Student_count_number.txt"
json_file_name = "ITT_Student.json"
key_list = ["이름","나이","주소"]
key_list_2 = ["강의코드","강의명","강사"]

def tree_maker():
    for x in range(1, 10 * 2, 2):
        print((" " * ((10 * 2 - 1 - x) // 2)) + ("*" * x))
    for y in range(1, 4):
        print(" " * (10 - 2) + "***")


def st_ID_Generator():
    try:
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

def check_value_ID(input_data,key_data):
    for dic_data in t:
        if input_data in dic_data[key_data]:
            return (dic_data[key_data])

def check_value_student(input_data,key_data):
    store = []
    tt = 0
    while True:
        if tt < len(t):
            for dic_data in t:
                if input_data in dic_data["학생정보"][key_data]:
                    store.append(dic_data["학생정보"][key_data])
                    tt += 1
        return (store)

def check_value_academy(input_data,key_data):
    for dic_data in t:
        if input_data in dic_data["수강정보"][key_data]:
            return (dic_data["수강정보"][key_data])

def check_value_class(input_data,key_data):
    for dic_data in t:
        for x in range(len(dic_data["수강정보"]) - 1):
            if input_data in dic_data["수강정보"]["강좌"+str(x)][key_data]:
                return (dic_data["수강정보"]["강좌"+str(x)][key_data])

def fix_json_file():
    print("변경된 데이터를 저장 중입니다")
    with open(os.getcwd() + os_delimeter + json_file_name, 'w', encoding="utf-8") as make_file:
        readable_result = json.dumps(t, indent=4, ensure_ascii=False)
        make_file.write(readable_result)
        print('저장이 완료되었습니다')

def output_personel_information(personal_sentence):
    if len(personal_sentence) == 1:  #
        for i in range(len(t)):
            for x in range(len(t[i]["수강정보"]) - 1):
                if personal_sentence == t[i]["학생ID"] or personal_sentence == \
                        t[i]["학생정보"]["이름"] or personal_sentence == \
                        t[i]["학생정보"]["나이"] or personal_sentence == \
                        t[i]["학생정보"]["주소"]:
                    print("\n")
                    print((("\t" * 13) + "학생ID: %s\n" % t[i]["학생ID"]) + "\n" +
                          (("\t" * 12) + "이름: %s" % t[i]["학생정보"]["이름"]) + "\n" +
                          (("\t" * 12) + "나이: %s" % t[i]["학생정보"]["나이"]) + "\n" +
                          (("\t" * 12) + "주소: %s" % t[i]["학생정보"]["주소"]) + "\n\n" +
                          (("\t" * 13) + "과거수강횟수: %s" % t[i]["수강정보"]["과거수강횟수"]) + "\n")
                    print((("\t" * 14) + "강좌" + str(x + 1)) + "\n\n" +
                          (("\t" * 13) + "강의코드" + str(x + 1) + ": " + "%s" %
                           t[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n" +
                          (("\t" * 13) + "강의명" + str(x + 1) + ": " + "%s" %
                           t[i]["수강정보"]["강좌" + str(x)]["강의명"]) + "\n" +
                          (("\t" * 13) + "강사" + str(x + 1) + ": " + "%s" %
                           t[i]["수강정보"]["강좌" + str(x)]["강사"]) + "\n" +
                          (("\t" * 13) + "개강일" + str(x + 1) + ": " + "%s" %
                           t[i]["수강정보"]["강좌" + str(x)]["개강일"]) + "\n" +
                          (("\t" * 13) + "종료일" + str(x + 1) + ": " + "%s" %
                           t[i]["수강정보"]["강좌" + str(x)]["종료일"]) + "\n")
                    continue
    if len(personal_sentence) >= 2:
        for i in range(len(t)):
            for x in personal_sentence:
                if x == t[i]["학생ID"] or x == t[i]["학생정보"]["이름"] or x == t[i]["학생정보"]["나이"] or x == t[i]["학생정보"]["주소"]:
                    print((("\t" * 1) + "학생ID: %s\n" % t[i]["학생ID"]))
                    break



def output_institute_information(institute_sentence):
    for i in range(len(t)):
        for x in range(len(t[i]["수강정보"]) - 1):
            if institute_sentence == t[i]["수강정보"][
                "과거수강횟수"] or institute_sentence == t[i]["수강정보"]["강좌" + str(x)][
                "강의코드"] or institute_sentence == t[i]["수강정보"]["강좌" + str(x)][
                "강의명"] or institute_sentence == t[i]["수강정보"]["강좌" + str(x)][
                "강사"]:
                print("\n")
                print((("\t" * 13) + "학생ID: %s\n" % t[i]["학생ID"]) + "\n" +
                      (("\t" * 12) + "이름: %s" % t[i]["학생정보"]["이름"]) + "\n" +
                      (("\t" * 12) + "나이: %s" % t[i]["학생정보"]["나이"]) + "\n" +
                      (("\t" * 12) + "주소: %s" % t[i]["학생정보"]["주소"]) + "\n\n" +
                      (("\t" * 13) + "과거수강횟수: %s" % t[i]["수강정보"]["과거수강횟수"]) + "\n")
                print((("\t" * 14) + "강좌" + str(x + 1)) + "\n\n" +
                      (("\t" * 13) + "강의코드" + str(x + 1) + ": " + "%s" %
                       t[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n" +
                      (("\t" * 13) + "강의명" + str(x + 1) + ": " + "%s" %
                       t[i]["수강정보"]["강좌" + str(x)]["강의명"]) + "\n" +
                      (("\t" * 13) + "강사" + str(x + 1) + ": " + "%s" %
                       t[i]["수강정보"]["강좌" + str(x)]["강사"]) + "\n" +
                      (("\t" * 13) + "개강일" + str(x + 1) + ": " + "%s" %
                       t[i]["수강정보"]["강좌" + str(x)]["개강일"]) + "\n" +
                      (("\t" * 13) + "종료일" + str(x + 1) + ": " + "%s" %
                       t[i]["수강정보"]["강좌" + str(x)]["종료일"]) + "\n")
                continue

output_personel_information(check_value_student("김기","이름"))