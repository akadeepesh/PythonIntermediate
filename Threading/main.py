import threading

def func1():
    for i in range(100):
        print("1")

def func2():
    for i in range(100):
        print("2")

func1Thread = threading.Thread(target=func1) # This will create a new thread which will execute the func1 function
func2Thread = threading.Thread(target=func2)

func1Thread.start()
func2Thread.start()

func1Thread.join() # This will make sure that the main thread waits for the func1Thread to finish
func2Thread.join() # This will make sure that the main thread waits for the func2Thread to finish

print("Hello World") # This will be printed after both the threads are done executing

