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

def getTourPointChinese(yyyymm,natCd,edCd,nPagenum,nItems):

    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM="+yyyymm
    parameters += "&NAT_CD=" + urllib.parse.quote(natCd)
    parameters += "&ED_CD=" + urllib.parse.quote(edCd)
    parameters += "&RES_NM=&pageNo=" + str(nPagenum)
    parameters += "&natCdOfRows" + str(nItems)
    url = end_point + parameters
    retData = get_request_url(url)

    if (retData == None):
        return None

    else:
        return json.loads(retData)

def getTourPointData(item, yyyymm,jsonResult):
    ed = ''if 'ed' not in item.keys() else item['ed']
    edCd = ''if 'edCd' not in item.keys() else item['edCd']
    natCd = ''if 'natCd' not in item.keys() else item['natCd']
    natKorNm = ''if 'natKorNm' not in item.keys() else item['natKorNm']
    num = '' if 'num' not in item.keys() else item['num']

    jsonResult.append({'yyyymm':yyyymm,'ed':ed,'edCd':edCd,"natCd":natCd,'natKorNm':natKorNm,
                       'num':num})
    return

def main():
    jsonResult = []
    edCd = "E"
    nItems = 100

    nStartYear = 2016
    nEndYear = 2017

    for year in range(nStartYear,nEndYear):
        for month in range(12,13):
            yyyymm = "{0}{1:0>2}".format(str(year),str(month))
            nPagenum = 1

            while True:
                global natCd
                for i in range(101,1000):
                    natCd = str(i)
                    jsonData = getTourPointChinese(yyyymm,natCd,edCd,nPagenum,nItems)
                    if(jsonData['response']['header']['resultMsg']=='OK'):
                        nTotal = jsonData['response']['body']['totalCount']
                        getTourPointData(jsonData['response']['body']['items']['item'], yyyymm, jsonResult)
                        # print(getTourPointData(jsonData['response']['body']['items']['item'][0]),yyyymm, jsonResult)
                        nPage = math.ceil(nTotal / 100)
    #
                        if nTotal ==0:
                            break
                        if (nPagenum == nPage):
                            break

                        nPagenum += 1
                    else:
                        break

    with open('%s_중국인 방문객 빅데이터 수집정보_ver1%d_%d.json' % (natCd, nStartYear, nEndYear - 1), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)
    print("%s_중국인 방문객 빅데이터 수집정보_%d_%d.json SAVED" % (natCd, nStartYear, nEndYear - 1))

if __name__ == '__main__':
    main()