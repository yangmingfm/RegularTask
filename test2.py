# -*- coding: UTF-8 -*-

''


def say(a=1, b=2):
    print a, b


def haha(**kw):
    # say(kw)
    apply(say, (), kw)

haha(a='a', b='b')

def testFunc(arg1,*kw,**nkw):
    print arg1
    print kw
    print nkw

testFunc(1,*(1,2),**{'1':2,'3':4})