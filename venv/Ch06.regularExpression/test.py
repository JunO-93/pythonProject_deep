import re

dates = [
    '2022/08/08',
    '1000/01/01',
    '9999/12/31',
    '900/12/31',
    '12000/10/26',
    '2021/13/01',
    '2023/2/02',
    '2022/06/3',
    '2022/06/36',
]


regex = '^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[0-1])$'

for date in dates:
    matchObj = re.match(regex,date)
    result = (lambda x : True if x else False)(matchObj)
    print(f"{date} {result}")


