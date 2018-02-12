import time
import weather_forcast
import json
import threading
import sys

g_Radiator = False
g_Gas_Valve = False
g_Door = False
g_Humidifier = False
g_Dehumidifier = False
g_AI_Mode = False

def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 인공지능 모드")
    print("4. 시뮬레이션 모드")
    print("5. 프로그램 종료")
    print("")

def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    elif devcie_status == False : print("정지")

def print_window_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("열림")
    elif devcie_status == False : print("닫힘")

def check_device_status():
    print("")
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_window_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문', g_Door)
    print_device_status('가습기',g_Humidifier)
    print_device_status('제습기',g_Dehumidifier)

def update_scheduler():
    while True:
        if g_AI_Mode == False:
            continue
        else:
            if time.strftime("%M%S") == "2740":
                print("")
                weather_forcast.main()
                time.sleep(3600)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기")
    print("7. 뒤로가기")
    print("")

def control_device():
    while True:
        global g_Radiator, g_Gas_Valve, , g_Door
        check_device_status()
        print_device_menu()
        menu_num = int(input("번호를 입력하세요: "))
        if menu_num == 1: g_Radiator = not g_Radiator
        if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
        if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
        if menu_num == 4: g_Door = not g_Door
        if menu_num == 5: break
        check_device_status()
        return None

def loading():
    _print('■ ')
    time.sleep(1)
    _print('■ ■ ■ ')
    time.sleep(1)
    _print('■ ■ ■ ■ ■')
    time.sleep(1)
    _print(' 👌')

def vertual_file(value):
    jsonResult = []
    now = time.localtime()
    base_date = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    base_time = "%02d%02d" % (now.tm_hour - 1, now.tm_min)
    nx = "89"
    ny = "91"
    jsonData = weather_forcast.getNatVisitor(base_date, base_time, nx, ny)
    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for i in range(len(jsonData['response']['body']['items']['item'])):
            if jsonData['response']['body']['items']['item'][i]["category"] == value:
                baseDate = jsonData['response']['body']['items']['item'][i]["baseDate"]
                baseTime = jsonData['response']['body']['items']['item'][i]["baseTime"]
                category = jsonData['response']['body']['items']['item'][i]["category"]
                fcstDate = jsonData['response']['body']['items']['item'][i]["fcstDate"]
                fcstTime = jsonData['response']['body']['items']['item'][i]["fcstTime"]
                fcstValue = jsonData['response']['body']['items']['item'][i]["fcstValue"]
                nx = jsonData['response']['body']['items']['item'][i]["nx"]
                ny = jsonData['response']['body']['items']['item'][i]["ny"]

                jsonResult.append({'basedate': baseDate, 'basetime': baseTime, 'category': category, 'fcstDate': fcstDate,
                               'fcstTime': fcstTime,'fcstValue': fcstValue, 'fcs''nx': nx, 'ny': ny})
    return jsonResult

def vertual_simulation_balcony():
    global g_Balcony_Windows
    json_big_data = vertual_file("PTY")
    for num in range(len(json_big_data)):
        json_big_data[num]["fcstValue"] = 1
    print("<<현재 환경 출력>>")
    print_window_status('발코니(베란다) 창문', g_Balcony_Windows)
    loading()
    value = 0
    category_count = 0
    for num in range(len(json_big_data)):
        if json_big_data[num]["category"] == "PTY":
            category_count += 1
            value += json_big_data[num]["fcstValue"]
            if value / category_count > 0:
                if g_Balcony_Windows == True:
                    print("\n비가 예상됩니다. 창문을 닫겠습니다")
                    g_Balcony_Windows = False
                    break
            elif value / category_count == 0:
                if g_Balcony_Windows == False:
                    print("날씨가 계속 맑은 예정입니다. 창문을 열겠습니다")
                    g_Balcony_Windows = True
    check_device_status()

def vertual_simulation_humid():
    global g_Humidifier
    json_big_data = vertual_file("REH")
    for num in range(len(json_big_data)):
        json_big_data[num]["fcstValue"] = 20
    print("<<현재 환경 출력>>")
    print_device_status('가습기', g_Humidifier)
    loading()
    for num in range(len(json_big_data)):
        if json_big_data[num]["category"] == "REH":
            if json_big_data[num]["fcstValue"] <= 30:
                if g_Humidifier == False:
                    print("\n실내가 건조합니다. 가습기를 작동합니다 ")
                    g_Humidifier = True
    check_device_status()

def vertual_simulation_dehumid():
    global g_Dehumidifier
    json_big_data = vertual_file("REH")
    for num in range(len(json_big_data)):
        json_big_data[num]["fcstValue"] = 80
    print("<<현재 환경 출력>>")
    print_device_status('제습기', g_Dehumidifier)
    loading()
    for num in range(len(json_big_data)):
        if json_big_data[num]["category"] == "REH":
            if json_big_data[num]["fcstValue"] >= 70:
                if g_Dehumidifier == False:
                    print("\n실내가 습합니다. 제습기를 작동합니다 ")
                    g_Dehumidifier = True
    check_device_status()

def vertual_simulation_sunny():
    global g_Humidifier, g_Dehumidifier
    json_big_data = vertual_file("REH")
    for num in range(len(json_big_data)):
        json_big_data[num]["fcstValue"] = 60
    print("<<현재 환경 출력>>")
    print_device_status('가습기',g_Humidifier)
    print_device_status('제습기',g_Dehumidifier)
    loading()
    for num in range(len(json_big_data)):
        if json_big_data[num]["category"] == "REH":
            if 30 < json_big_data[num]["fcstValue"] < 70:
                if g_Humidifier == True:
                    print("\n날씨가 상쾌합니다. 가습기 작동을 중지합니다")
                    g_Humidifier = False
                elif g_Dehumidifier == True:
                    print("날씨가 상쾌합니다. 제습기 작동을 중지합니다")
                    g_Dehumidifier = False
    check_device_status()

def smart_mode_Balcony():
    global g_Balcony_Windows
    with open("날씨예보정보.json", encoding="utf-8") as json_data:
        json_data_load = json.load(json_data)
        json_data_string = json.dumps(json_data_load)
        json_big_data = json.loads(json_data_string)

        value = 0
        category_count = 0

        for num in range(len(json_big_data)):
            if json_big_data[num]["category"] == "PTY":
                category_count += 1
                value += json_big_data[num]["fcstValue"]
                if value/category_count > 0:
                    if g_Balcony_Windows == True:
                        print("비가 예상됩니다. 창문을 닫겠습니다")
                        g_Balcony_Windows = False
                        break
                elif value/category_count == 0:
                    if g_Balcony_Windows == False:
                        print("날씨가 계속 맑은 예정입니다. 창문을 열겠습니다")
                        g_Balcony_Windows = True
                        break

def smart_mode_de_hu():
    global g_Humidifier, g_Dehumidifier
    with open("날씨예보정보.json", encoding="utf-8") as json_data:
        json_data_load = json.load(json_data)
        json_data_string = json.dumps(json_data_load)
        json_big_data = json.loads(json_data_string)

        for num in range(len(json_big_data)):
            if json_big_data[num]["category"] == "REH":
                if json_big_data[num]["fcstValue"] <= 30:
                    if g_Humidifier == False:
                        print("실내가 건조합니다. 가습기를 작동합니다 ")
                        g_Humidifier = True
                    elif g_Dehumidifier == True:
                        print("실내가 건조합니다 제습기를 중지합니다")
                        g_Dehumidifier = False
                    break

                elif json_big_data[num]["fcstValue"] >= 70:
                    if g_Dehumidifier == False:
                        print("실내가 습합니다. 제습기를 작동합니다 ")
                        g_Dehumidifier = True
                    elif g_Humidifier == True:
                        print("실내가 건조합니다 가습기를 중지합니다")
                        g_Humidifier = False
                    break

                elif 30 < json_big_data[num]["fcstValue"] < 70:
                    print("")
                    print("쾌적한 환경입니다. 제,가습기를 가동하지 않아도 됩니다.")
                    print("")
                    break

def smart_mode():
    while True:
        global  g_AI_Mode
        print("")
        print("1. 인공지능 모드 상태 확인")
        print("2. 인공지능 모드 상태 변경")
        print("3. 실시간 기상정보 Update")
        print("4. 뒤로가기")
        menu_num = int(input("메뉴를 선택하세요: "))

        if menu_num == 1:
            print("")
            print("현재 인공지능 모드: ", end="")
            if g_AI_Mode == True:
                print("작동")
            else:
                print("정지")
        elif menu_num == 2:
            g_AI_Mode = not g_AI_Mode
            print("")
            print("현재 인공지능 모드: ", end="")
            if g_AI_Mode == True:
                print("작동")
                print("")
                print("현재 환경에 따른 디바이스 조정 중")
                loading()
                print("")
                smart_mode_Balcony()
                smart_mode_de_hu()
                check_device_status()
            else:
                print("정지")
                print("")
        elif menu_num == 3:
            weather_forcast.main()
            print("업데이트에 따른 디바이스 조정 중")
            loading()
            print("")
            if g_AI_Mode == True:
                smart_mode_Balcony()
                smart_mode_de_hu()
                check_device_status()
            elif g_AI_Mode == False:
                print("AI 모드가 꺼져있어 디바이스를 조정할수없습니다.")
        elif menu_num == 4:
            break

def simulation_mode():
    while True:
        print("\n1. 비오는 날 시뮬레이션")
        print("2. 건조한 날 시뮬레이션")
        print("3. 습한 날 시뮬레이션")
        print("4. 상쾌한 날 시뮬레이션")
        print("5. 뒤로가기")
        menu_num = int(input(">>"))
        if menu_num == 1:
            vertual_simulation_balcony()
        elif menu_num == 2:
            vertual_simulation_humid()
        elif menu_num == 3:
            vertual_simulation_dehumid()
        elif menu_num == 4:
            vertual_simulation_sunny()
        elif menu_num == 5:
            break
        else:
            print("잘못입력하셨습니다")
            continue


print("-"*100)
print("\t\t\t\t\t""<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("-"*100)
while True:
    t = threading.Thread(target=update_scheduler)
    t.daemon = True
    t.start()
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))
    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num ==3):
        smart_mode()
    elif(menu_num ==4):
        simulation_mode()
    elif (menu_num ==5):
        break
