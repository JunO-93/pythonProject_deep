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
        print(f"[sub] {self.name} end")


if __name__ == "__main__":
    print("[main] start")
    p = Subprocess(name='이름이다')
    p.start()
    p.join()
    print("[main] end")