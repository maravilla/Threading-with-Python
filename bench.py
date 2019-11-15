import threading
import time
import random
from multiprocessing import Process

def executeThread(i):
    print("Thread() started".format(i))
    sleepTime = random.randint(1,10)
    time.sleep(sleepTime)
    print("Thread() finished executing".format(i))

def runExecuteThread():
    for i in range (10):
        thread = threading.Thread(target = excecuteThread, )

def calculatePrimeFactors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while(n%d) == 0:
            primfac.append(n)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

def executeProc():
    for i in range(1000):
        rand = random.randint(20000, 10000000)
       # print(calculatePrimeFactors(rand))


def myThread(i):
	print("Thread(): started".format(i))
	time.sleep(random.randint(1,5))
	print("Thread(): finished".format(i))

def myChildThread():
	print("Child Thread Starting")
	time.sleep(5)
	print("Current Thread --------------")
	print(threading.current_thread())
	print("-----------------------------")
	print("Main Thread -----------------")
	print(threading.main_thread())
	print("-----------------------------")
	print("Child Thread Ending")


def myNamedThread():
	print("Thread {} starting".format(threading.currentThread().getName()))
	time.sleep(10)
	print("Thread {} ending".format(threading.currentThread().getName()))


def myWorker():
	t1 = time.time()
	print("Process started at: {}".format(t1))
	time.sleep(20)
print("2. Comparative of single thead, multiprocessing and multi-thread")


for i in range(10):
    thread2 = threading.Thread(target=executeThread, args=(i,))
    thread2.start()
    print("Active Threads: ", threading.enumerate())


print("Starting number crunching")
t0 = time.time()
threads = []

print("1. Multiple Threads")

for i in range(10):
    thread = threading.Thread(target = executeProc())
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

t1 = time.time()
totalTime = t1 - t0
print("Execution Time: {}".format(totalTime))

print("3. Total Number of Active Threads")

for i in range(random.randint(2,50)):
	thread3 = threading.Thread(target=myThread, args=(i,))
	thread3.start()

time.sleep(4)

print("Total Number of Active Threads: {}".format(threading.active_count()))
print("4. Current ID Thread")

child = threading.Thread(target = myChildThread)
child.start()
child.join()

print("5. Enumerate threads")



for i in range(4):
	thread4 = threading.Thread(target=myThread, args=(i,))
	thread4.start()
print("Enumerating: {}".format(threading.enumerate()))

print("7. Thread ID")

for i in range(4):
	threadName = "Thread-" + str(i)
	thread5 = threading.Thread(name=threadName, target=myNamedThread)
	thread5.start()
print("{}".format(threading.enumerate()))

print("8. Stopping Threads mechanism")

myProcess = Process(target=myWorker)
print("Process: {}".format(myProcess))
myProcess.start()
print("Terminating Process...")
myProcess.terminate()
myProcess.join()
print("Process Terminated: {}".format(myProcess))


