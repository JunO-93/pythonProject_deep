from multiprocessing import Process
import time

# 클래스로 서브 프로세스 만드는법
# Process 상속
class Subprocess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")

if __name__ == "__main__":
    print("[main] start")
    p = Subprocess(name='이름이다')
    p.start()
    time.sleep(1)

    # 프로세스가 살아있는지 검사
    if p.is_alive():
        p.terminate() # 프로세스가 살아있다면 강제종료할 때 사용하는 방법
    print("[main] end")


# 추가학습
# 1. 스레드간 데이터 처리(lock)
# 2. 프로세스간 데이터 전송 (Queue, Pipe)
# 3. 속도 비교
# 4. 운영체제와 메모리
# 5.