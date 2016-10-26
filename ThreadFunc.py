# -*- coding: UTF-8 -*-

''

class ThreadFunc(object):
    ''
    def __init__(self,func,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs
        self.func = func

    def __call__(self):
        self.func(self.args,self.kwargs)

class Taks(ThreadFunc):
    ''
