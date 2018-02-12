from urllib.request import urlopen
# urllib library 에서 request 모듈 중 urlopen 함수를 import 한다는 뜻
html = urlopen("https://pythonscraping.com/pages/page1.html")
print(html.read())

# urllib : 웹을 통해 데이터를 요청하는 함수, 쿠키를 처리하는 함수, 헤더나 유저 에이전트 같은
# 메타데이터를 바꾸는 함수 등이 있다.

# urlopen : 네트워크를 통해 원격 객체를 읽는다, Html 파일이나 이미지, 기타 파일 스트림을 쉽게 열수 있는
# library 이다