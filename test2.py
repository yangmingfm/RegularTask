# -*- coding: UTF-8 -*-

''


def say(a=1, b=2):
    print a, b


def haha(**kw):
    # say(kw)
    apply(say, (), kw)

haha(a='a', b='b')

def mSay(a,b):
    print a,b

def test():
    apply(mSay,(),a=1,b=2)

test()