# -*- coding: UTF-8 -*-

''

from time import ctime,sleep
import threading

class ThreadFunc(object):
    ''
    def __init__(self,func,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs
        self.func = func
        print args
        print kwargs

    def __call__(self):
        ''
        self.func(self.args,self.kwargs)

class Task(ThreadFunc):
    ''


def testFunc():
    print 'test func'

task = Task(testFunc,*(1,2),**{'2':1})