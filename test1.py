# -*- coding: UTF-8 -*-

''

import thread,threading
from time import sleep,ctime

def loop(sleepTime,lock,loopIndex):
    sleep(sleepTime)
    print 'loop: ',' sleep over','end time ',ctime()
    lock.release()

def loop2(loopIndex,sleepTime):
    print 'loopIndex->',loopIndex,' begin loop at ',ctime()
    sleep(sleepTime)
    print 'sleep over at ',ctime()

def testThreadModule():
    ''
    loopTimeTable = [1,5]
    locks = []

    print 'begin time ',ctime()
    for i in range(0,len(loopTimeTable)):
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in range(0,len(loopTimeTable)):
        thread.start_new_thread(loop,(loopTimeTable[i],locks[i],i))

    for i in range(0,len(loopTimeTable)):
        while locks[i].locked():pass

def testThreadingModule():
    ''
    loopTimeTable = [2,4]
    threadTable = []

    for i in range(0,len(loopTimeTable)):
        newThread = threading.Thread(target=loop2,args=(i,loopTimeTable[i]))
        threadTable.append(newThread)

    for i in range(0,len(loopTimeTable)):
        threadTable[i].start()

    for i in range(0,len(loopTimeTable)):
        threadTable[i].join()



if __name__ == '__main__':
    # testThreadModule()
    testThreadingModule()