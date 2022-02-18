import re
datas = [
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.com',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver',
]


regex = re.compile('^([\w\-\_]{1,})@([\w\-]{1,})\.([\w]{1,})$')

for data in datas:
    matchObj = regex.match(data)
    result =(lambda x : True if x else False)(matchObj)
    print(f"{data} {result}")
