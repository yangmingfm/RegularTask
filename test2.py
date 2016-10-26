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
    for each in kw:
        print each
    for each in nkw:
        print each

testFunc(1,*(1,2),**{'1':2,'3':4})