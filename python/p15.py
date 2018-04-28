# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque
import hashlib
import binascii

# Disc #1 has 17 positions; at time=0, it is at position 1.
# Disc #2 has 7 positions; at time=0, it is at position 0.
# Disc #3 has 19 positions; at time=0, it is at position 2.
# Disc #4 has 5 positions; at time=0, it is at position 0.
# Disc #5 has 3 positions; at time=0, it is at position 0.
# Disc #6 has 13 positions; at time=0, it is at position 5.

discs = [
    (1, 17),
    (0, 7),
    (2, 19),
    (0, 5),
    (0, 3),
    (5, 13),
    (0, 11)
]

# test
# Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1.
# discs = [
#    (4, 5),
#    (1, 2)
#]

def current(discs):
    return [i for i, j in discs]


def tick(discs):
    return [((i + 1) % j, j) for i, j in discs]


def get_soln(discs):
    return [(j - idx) % j for idx, (i, j) in enumerate(discs)]


soln = get_soln(discs)

print "solution: {}".format(soln)

t = 0
while True:
    discs = tick(discs)
    
    state = current(discs)
    if state == soln:
        print "line up at t = {}".format(t)
        print "discs: {}".format(discs)
        break

    # print "{} {}".format(t, discs)

    t += 1

