import urllib.request
import datetime
import json
import math

access_key = "i4zXtlcTwh041E8W0qOyGPnIggToM4lqBePqd5ZR8v4uJQ6WcXACinkJgll%2Fk0PYSSinPNRJL%2B07OvnTXPcHaA%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')

    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def getTourPointChinese(yyyymm,sexCd,portCd,ageCd,nPagenum,nItems):

    end_point = "http://openapi.tour.go.kr/openapi/service/TourismIndustStatsService/getOvseaTuristStatsList"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM="+yyyymm
    parameters += "&SEX_CD=" + urllib.parse.quote(sexCd)
    parameters += "&AGE_CD=" + urllib.parse.quote(portCd)
    parameters += "&PORT_CD=" + urllib.parse.quote(ageCd)
    parameters += "&RES_NM=&pageNo=" + str(nPagenum)
    parameters += "&numOfRows" + str(nItems)

    url = end_point + parameters
    retData = get_request_url(url)

    if (retData == None):
        return None

    else:
        return json.loads(retData)

def getTourPointData(item,yyyymm,jsonResult):


    num = 0 if 'num' not in item.keys() else item['num']



    jsonResult.append{['yyyymm':yyyymm,'age':age,'ageCd':ageCd]}
