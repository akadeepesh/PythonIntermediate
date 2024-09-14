import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f"Thread {thread_number} is waiting")
    semaphore.acquire()
    print(f"Thread {thread_number} is accessing the resource")
    time.sleep(10)
    print(f"Thread {thread_number} is done")
    semaphore.release()

for i in range(10):
    accessThread = threading.Thread(target=access, args=(i,))
    accessThread.start()
    time.sleep(1)