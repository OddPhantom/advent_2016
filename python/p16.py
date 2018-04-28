# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque
import hashlib
import binascii



def checksum(data):

    to_checksum = data
    while True:
        pairs = zip(to_checksum[0::2], to_checksum[1::2])
        chksum = [1 if i == j else 0 for i, j in pairs]
        if len(chksum) % 2 == 1:
            break

        to_checksum = chksum

    return chksum


def process(data):

    r = [1 if i == 0 else 0 for i in data]
    r.reverse()

    data.append(0)
    data.extend(r)

    return data
    


def go(start_data, length_needed):


    data = list(start_data)

    while length_needed > len(data):
        data = process(data)


    d = data[:length_needed]
    chk = checksum(d)


    return d, chk




d, chk = go([int(i) for i in list("10000")], 20)

print d

print chk



d = [int(i) for i in list("01111010110010011")]
needed = 35651584


out, chk = go(d, needed)

#print "".join([str(x) for x in out])

print "".join([str(x) for x in chk])
