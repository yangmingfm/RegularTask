# -*- coding: UTF-8 -*-

''

import threading
from time import ctime,sleep

class RegularTask():
    ''
    def __init__(self):
        self.timer = None
        self.cycleTime = 0
        self.taskClass = None
        self.taskLiveTime = -1
        self.args = None
        self.kwargs = None
        self.turnUp = True

    def setTaskCycleTime(self,cycleTime):
        self.cycleTime = cycleTime

    def setTaskLiveTime(self,liveTime):
        self.taskLiveTime = liveTime

    def setTask(self,taskClass,taskFunc):
        self.taskClass = taskClass
        self.taskFunc = taskFunc

    def setTaskArgs(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def executeFunc(self):
        pass

    def executeClass(self):
        pass

    def beginTask(self):
        while True and self.turnUp:

        pass

