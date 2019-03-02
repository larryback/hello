#!/usr/bin/env python

from pprint import pprint
import sys

samples = [
    (2001, 23),
    (2002, 7),
    (2002, -12),
    (2001, 21),
    (2003, 20),
    (2005, 13),
    (2003, 3),
    (2005, -2),
    (2003, 22),
    (2001, -3),
]

samples.sort()
# pprint(samples)

def fn2():
    ret = {}
    prekey = None
    premax = -sys.maxsize
    for i in samples:
        (key, val) = i
        if key != prekey:
            # ret[key] = val
            premax = -sys.maxsize

        if premax < val:
            ret[key] = val
            premax = val
            print(":>>", key, val, premax)

        prekey = key

    pprint(ret)

def fn1():
    ret = {}
    prekey = None
    for i in samples:
        # key = i[0]
        # val = i[1]
        (key, val) = i
        if key != prekey:
            ret[key] = [val]
            prekey = key

        else:
            lst = ret[key]
            lst.append(val)

    pprint(ret)
    for y, l in ret.items():
        print(y, max(l))

<<<<<<< HEAD
fn2()
=======
#fn2()
fn1()
>>>>>>> bc0bbb4bf15e08a390da158eaef399fc0a0c9a26
