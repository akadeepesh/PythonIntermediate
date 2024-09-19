import threading

event = threading.Event()

def waiting():
    print("Waiting for event to be triggered...\n")
    event.wait()
    print("Hello DeCoder")

my_thread = threading.Thread(target=waiting)
my_thread.start()

x = input("Do you want to trigger the tread? (y/N) :")
if(x == "y" or x == "Y"):
    event.set()
