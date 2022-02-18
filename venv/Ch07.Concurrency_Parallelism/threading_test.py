import threading

# 스레드에서 실행할 함수
def work():
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>>",)
    print(f"[sub] {keyword}로 검색을 시작합니다...")
    print("[sub] end")


# 메인스레드 실행되는 부분
print("[main] start")
worker = threading.Thread(target=work) # 스레드 객체
worker.daemon = True # 메인 스레드가 종료가 될때 같이 종료가 된다
worker.start() # 스레드 실행
print("[main] 메인 스레드는 자기 할일을 합니다.")
print("[main] end")




