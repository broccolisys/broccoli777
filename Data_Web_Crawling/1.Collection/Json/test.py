if del_number == 2:
    print("-" * 140)
    print(("해당된 ID의 수강정보 입니다").center(110))
    print("-" * 140)
    print("")
    for i in range(len(open_json_file())):
        if input_value == open_json_file()[i]["학생ID"]:
            for x in range(len(open_json_file()[i]["수강정보"]) - 1):
                print(((("\t" * 12) + "강좌" + str(x + 1)) + " - " + "강의코드" + str(x + 1) + ": " + "%s" %
                       open_json_file()[i]["수강정보"]["강좌" + str(x)]["강의코드"]) + "\n")
                continue
    print("-" * 140)
    print("삭제할 강좌의 강의 코드를 입력하세요(강좌 전체 삭제:ALL,뒤로가기:0)")
    del_code = str(input(":"))
    if del_code == "ALL" or del_code == "all" or del_code == "All" or del_code == "aLL":
        del_agree = str(input("수강 정보를 삭제하시겠습니까? Y/N"))
        if del_agree == "Y" or del_agree == "y":
            del (json_big_data[i]["수강정보"])
            print("수강 정보를 삭제하였습니다")
            check_del_save()
        if del_agree == "N" or del_agree == "n":
            print("취소하였습니다")
            continue