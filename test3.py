# -*- coding: UTF-8 -*-

''

class unknownClass(object):
    ''
    def __init__(self,val):
        self.val = val
        print val

    def __call__(self):
        print 'call',self.val

    def getVal(self):
        return self.val

print unknownClass(3).getVal()

a = unknownClass(3)

a()