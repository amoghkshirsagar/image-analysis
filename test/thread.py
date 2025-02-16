from time import sleep, time
from random import randint
from threading import Thread

start = time()
def printMessage(message):
    sleep(randint(1, 5))
    print(message)

printMessage("start")

def test():
    for i in range(10):
        printMessage("test")

def ans():
    for i in range(10):
        printMessage("answer")

threadT = Thread(target=test)
threadT.start()

threadA = Thread(target=ans)
threadA.start()

print("before Joining Test")
threadT.join()
print("after Joining Test")
print("before Joining Answer")
threadA.join()
print("after Joining Answer")
print("mid")

end = time()
duration = end - start
print(f"Duration: {duration} seconds")

print("end")
