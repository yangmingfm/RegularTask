# -*- coding: UTF-8 -*-

''

from time import ctime,sleep
import threading
import ThreadFunc

def testFunc():
    i = 0
    while True:
        print 'hello ',i
        sleep(1)
        i+=1

newThread = threading.Thread(target=testFunc())
newThread.start()
newThread.join(10)
print 'over join'