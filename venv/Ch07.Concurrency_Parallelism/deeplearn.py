# 쓰레드와 데드락

import threading, queue, time

work = queue.Queue()

# def generagtor(start, end):
#     for i in range(start, end, 1):
#         work.put(i)

# def display():
#     while work.empty() is False:
#         data = work.get()
#         print(f"data is {str(data)}")
#         time.sleep(1)
#         work.task_done()

# threading.Thread(target=generagtor, args=(1,10)).start()
# threading.Thread(target=display()).start()
# work.join()

##----------------------------------

data = 0
# 같은 작업을 했을 때 같은 공간에 연속해서 데이터가 담기므로 원하는 값이 안들어감
# 락을 통해서 동기화 처리를 해야함
lock = threading.Lock()
def generagtor(start, end):
    global data;
    for i in range(start, end, 1):
        # Lock 이 설정된 이상 다음 이 Lock을 호출할 때 쓰레드는 대기를 한다.
        lock.acquire()
        buf = data
        time.sleep(0.01)
        data = buf + 1
        # 사용이 끝나면 Lock을 해제한다.
        lock.release()

t1 = threading.Thread(target=generagtor, args=(1,10))
t2 = threading.Thread(target=generagtor, args=(1,10))

t1.start()
t2.start()

t1.join()
t2.join()

print(data)