#실습문제 시간을 분으로 입력

input_time = input("표준입력: ")
hour, minute = str,str

if input_time.find("분")==-1:
    hour = input_time.split("시간")[0]
    print(f"표준출력 : {int(hour) * 60}")

elif input_time.find("시간")==-1:
    minute = input_time.split("분")[0]
    print(f"표준출력 : {int(minute)}")

else:
    split_string = input_time.split("시간")
    hour = split_string[0]
    minute = split_string[1].split("분")[0]
    print(f"표준출력 : {int(hour) * 60 + int(minute)}")


# 강의 소스

# time = input("시간을 입력하세요>>>")
# #1. 분만 있는 경우
# #2. 시간만 있는 경우
# #3. 시간과 분이 있는 경우
#
# if time.find('시간') == -1:
#     # 분만 있는 경우 ex)30분
#     result = int(time.split('분')[0]) # result = ['30', '']
# else :
#     # 시간만 있는 경우
#     if time.find('분') == -1:
#         result = int(time.split('시간')[0]) * 60
#     # 시간과 분이 있는 경우 ex) 1시간 30분
#     else:
#         sub = time.split('시간')
#         result = int(sub[0]) * 60 + int(sub[1].split('분')[0])# ['1',' 30분']
#
# print(result)