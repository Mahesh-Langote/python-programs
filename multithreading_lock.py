import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        for _ in range(100000):
            counter += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Counter Value:", counter)
