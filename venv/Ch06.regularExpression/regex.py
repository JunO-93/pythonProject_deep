import re

# 1. re 모듈 메서드

str = 'love people around you. love your work, love yourself'

# 1) match : 문자열의 처음부터 검색, 1개의 match 객체
result = re.match('love',str)
print(result)

# 2) search : 문자열의 모든부분을 검색, 1개의 match 객체

result = re.search('people',str)
print(result)

# 3) findall : 문자열의 전체를 검색 (결과 : 문자열 리스트)
results = re.findall('love',str)
print(results)

# 4) finditer : 문자열의 전체를 검색 (결과 : match 객체 이터레이터)
results = re.finditer('love',str)
print(results)

for result in results:
    print(result)

# 5) fullmatch 패턴과 문자열이 완벽하게 일치하는지 검사
str2 = 'Hey Guys, read books'
result = re.fullmatch('.*', str2)
print(result)

# 2. match object의 메서드
result = re.search('people', str)

# 1) group() : 매칭된 문자열을 반환
print(result.group())

# 2) start() : 매칭된 문자열의 시작 위치를 반환
print(result.start())

# 3) end() : 매칭된 문자열의 끝 위치를 반환
print(result.end())

#4) span() : 매칭된 문자열의 (시작, 끝) 위치 튜플을 반환
print(result.span())



# 정규식 활용 연습
str3 = {"dayLpDataInfoList":[{"custNo":"1029388867","meterNo":"25202027064","mr_ymd":"20220101","multi_meter_yn":"N","pwr_qty0015":82.87,"pwr_qty0030":80.64,"pwr_qty0045":81.94,"pwr_qty0100":99.32,"pwr_qty0115":123.66,"pwr_qty0130":110.56,"pwr_qty0145":61.06,"pwr_qty0200":43.78,"pwr_qty0215":1.55,"pwr_qty0230":0.83,"pwr_qty0245":0.83,"pwr_qty0300":0.83,"pwr_qty0315":0.83,"pwr_qty0330":0.83,"pwr_qty0345":0.83,"pwr_qty0400":0.83,"pwr_qty0415":0.83,"pwr_qty0430":0.83,"pwr_qty0445":0.83,"pwr_qty0500":0.83,"pwr_qty0515":0.83,"pwr_qty0530":0.83,"pwr_qty0545":0.83,"pwr_qty0600":0.83,"pwr_qty0615":0.83,"pwr_qty0630":5.26,"pwr_qty0645":9.43,"pwr_qty0700":1.19,"pwr_qty0715":12.17,"pwr_qty0730":44.1,"pwr_qty0745":66.74,"pwr_qty0800":46.08,"pwr_qty0815":22.1,"pwr_qty0830":42.98,"pwr_qty0845":85,"pwr_qty0900":92.99,"pwr_qty0915":63.5,"pwr_qty0930":68.58,"pwr_qty0945":112.28,"pwr_qty1000":87.05,"pwr_qty1015":40.9,"pwr_qty1030":45.97,"pwr_qty1045":54.94,"pwr_qty1100":64.12,"pwr_qty1115":70.13,"pwr_qty1130":92.2,"pwr_qty1145":59.72,"pwr_qty1200":40.64,"pwr_qty1215":30.24,"pwr_qty1230":51.91,"pwr_qty1245":84.31,"pwr_qty1300":78.19,"pwr_qty1315":44.39,"pwr_qty1330":51.48,"pwr_qty1345":67.25,"pwr_qty1400":46.73,"pwr_qty1415":29.56,"pwr_qty1430":27,"pwr_qty1445":46.69,"pwr_qty1500":31.5,"pwr_qty1515":23.15,"pwr_qty1530":58.68,"pwr_qty1545":58.28,"pwr_qty1600":30.89,"pwr_qty1615":15.37,"pwr_qty1630":43.49,"pwr_qty1645":69.84,"pwr_qty1700":51.23,"pwr_qty1715":46.19,"pwr_qty1730":39.31,"pwr_qty1745":55.26,"pwr_qty1800":54.4,"pwr_qty1815":25.56,"pwr_qty1830":40.9,"pwr_qty1845":32.87,"pwr_qty1900":39.96,"pwr_qty1915":77.18,"pwr_qty1930":91.44,"pwr_qty1945":48.96,"pwr_qty2000":22.82,"pwr_qty2015":32.29,"pwr_qty2030":69.48,"pwr_qty2045":"","pwr_qty2100":"","pwr_qty2115":"","pwr_qty2130":"","pwr_qty2145":44.39,"pwr_qty2200":25.67,"pwr_qty2215":46.69,"pwr_qty2230":32.8,"pwr_qty2245":31.18,"pwr_qty2300":63.54,"pwr_qty2315":105.98,"pwr_qty2330":74.74,"pwr_qty2345":38.88,"pwr_qty2400":49.79,"vld_pwr0100":"","vld_pwr0200":"","vld_pwr0300":"","vld_pwr0400":"","vld_pwr0500":"","vld_pwr0600":"","vld_pwr0700":"","vld_pwr0800":"","vld_pwr0900":"","vld_pwr1000":"","vld_pwr1100":"","vld_pwr1200":"","vld_pwr1300":"","vld_pwr1400":"","vld_pwr1500":"","vld_pwr1600":"","vld_pwr1700":"","vld_pwr1800":"","vld_pwr1900":"","vld_pwr2000":"","vld_pwr2100":"","vld_pwr2200":"","vld_pwr2300":"","vld_pwr2400":""}]}

import json


str3 = json.dumps(str3)
regex = re.compile('([0-9]*\.[0-9]*)?(?=,)')

result3 = regex.finditer(str3)

count = 0
count2 = 0
for result in result3:
    if result.group():
        print(f"search {result.group()}")
        count2 +=1
    count +=1
print(count, count2)
