# -*- coding: UTF-8 -*-

''

class RegularTask():
    ''
    def __init__(self):
        self.timer = None
        self.cycleTime = 0
        self.taskClass = None
        self.taskLiveTime = -1
        self.args = None
        self.kwargs = None
    def setTaskCycleTime(self,cycleTime):
        self.cycleTime = cycleTime

    def setTask(self,taskClass,taskFunc):
        self.taskClass = taskClass
        self.taskFunc = taskFunc

    def setTaksArgs(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def excuteTask(self,args):
        if self.taskClass != None:


