import threading
import time

path = "Threading/text.txt"
text = ""

def read_file():
    global text 
    with open(path, "r") as file:
        text = file.read()
    time.sleep(3)

def print_loop():
    for i in range(30):
        print(text)
        time.sleep(1)

daemon_thread = threading.Thread(target=read_file, daemon=True)
print_thread = threading.Thread(target=print_loop)

daemon_thread.start()
print_thread.start()