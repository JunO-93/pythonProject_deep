import threading
import time

# 주식 자동매매
# 매수, 매도

# 매수 스레드

def buyer():
    for i in range(5):
        print("[매수] 데이터 요청 중...")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 지금이 매수 타이밍 인가...")
        time.sleep(1)
        print("[매수] 풀매수 가자...")
        time.sleep(1)

# 매도 스레드
def saler():
    for i in range(5):
        print("[매수] 데이터 요청 중...")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 손절할까? 익절할까?...")
        time.sleep(1)
        print("[매수] 눈물을 머금고 손절합니다....")
        time.sleep(1)

# 메인 스레드
print("[메인] start")
buyer = threading.Thread(target=buyer)
saler = threading.Thread(target=saler)
buyer.start()
saler.start()

# 서브 스레드가 종료될 때 까지 메인 스레드가 기다림
buyer.join()
saler.join()

print("[메인] 장이 종료되었습니다.")