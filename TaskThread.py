# -*- coding: UTF-8 -*-

''

from time import ctime,sleep
import threading
import ThreadFunc

class TaskThread(threading.Thread):
    def __init__(self,liveTime,task,name = ''):
        threading.Thread.__init__(self)
        self.liveTime = liveTime
        self.name = name

    def setLiveTime(self,liveTime):
        self.liveTime = liveTime

    def run(self):
        taskThread = threading.Thread(target = ThreadFunc.Task)
        taskThread.setDaemon(False)
        taskThread.start()
        sleep(self.liveTime)
        if taskThread.isAlive():
