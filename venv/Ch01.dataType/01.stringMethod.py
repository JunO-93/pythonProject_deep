#1. replace 문자열 교체
a = '오늘 날씨는 흐림 입니다.'.replace("흐림","맑음")
print(a)

#2. find 문자열 찾기
# 문자 'Hello world'.find('world2') 없는 문자열일 경우 retrun 값 -1
b = 'Hello world'.find('world')
print(b)

#3. split 문자열 분리
c= '나이키신발 265 X1212 78000'.split()
print(c)

d = '나이키신발:265:X1212:78000'.split(':')
print(d)

#4. strip 문자열 공백제거

e = '       Yeah        '.lstrip()
f = '       Yeah        '.rstrip()
g = '       Yeah        '.strip()

print(e)
print(f)
print(g)