import threading
import time

x = 8192
lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached maximum")
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached minimum")
    lock.release()

halveThread = threading.Thread(target=halve)
doubleThread = threading.Thread(target=double)

halveThread.start()
doubleThread.start()