import math
import requests 
import sys

testContainer = ["test", "hello", "myWorld"]

# While 반복문.
index = 5
while index >= 1:
    print("index : " + str(index))
    index -= 1

# 컨테이너 사용법.
for testValue in testContainer:
    print(testValue)

def TestFuntion(userName):
     print("UserName : " + userName)
     radian = 0.0
     while(radian <= 1.0):
          print("cos value : " + str(math.cos(radian)))
          radian += 0.1
    
TestFuntion("opk4406")

# https://m.blog.naver.com/csgct/220444910779
# URL 주소에서 #같은 특수문자 처리에 대한 내용.

myBralwStarsTag = "#2LPCCQ0U0" 
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
myHomeApiKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImEzZmIxMGRhLTZmMzgtNGE0Yy1iZDJiLWIzYzI2NTAyYzVkNyIsImlhdCI6MTYwMjMxNzI5MSwic3ViIjoiZGV2ZWxvcGVyL2JlNTE3MjQ2LWNmYzgtZDQ5NC1hOTkxLWNjNGYzOWVhMWNmYSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTgyLjIyNC43Mi4yMTkiXSwidHlwZSI6ImNsaWVudCJ9XX0.pVNBskTcukhL8wGfvQ00kGBPCCBkse8hFctClFIsNaqWVh8nskJGm47UcWURa56Ti7UIISHEOwbcrwoF8QnkYA"
inCompanyKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjMxZTIzYzZiLTkwNGYtNGMzMy1hNWQzLWM5ZTA5M2QzOTJlMSIsImlhdCI6MTYwMjY0OTQ0MCwic3ViIjoiZGV2ZWxvcGVyL2JlNTE3MjQ2LWNmYzgtZDQ5NC1hOTkxLWNjNGYzOWVhMWNmYSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTA2LjI0Ny4yMjUuODIiXSwidHlwZSI6ImNsaWVudCJ9XX0.zDoyAKHTIGTzFsdyG_nPDh6UxzU5zNvPMQrLL3NckgMGgYqF9u_MPkanv_jh8uVpgpmdzrObMl2mLc2XDO-tyw"

battleLogURL = "https://api.brawlstars.com/v1/players/{0}/battlelog".format(myBralwStarsTag)
playerInfoURL = "https://api.brawlstars.com/v1/players/{0}".format(myBralwStarsTag)
bralwersURL = "https://api.brawlstars.com/v1/brawlers" # 브롤러 정보.

headers = {
'Content-Type': 'application/json; charset=utf-8',
'Accept': 'application/json',
'User-Agent': '{0}'.format(userAgent),
'Authorization': 'Bearer {}'.format(inCompanyKey)
}
response = requests.get(battleLogURL, headers)
print(response.text)
print(response.raise_for_status)
print(response.json)