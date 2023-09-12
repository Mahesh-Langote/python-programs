import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
