# -*- coding: utf-8 -*-
# from __future__ import division
import sys
import os
import helpers
from collections import deque
import hashlib
import binascii
import itertools

def get_adjacent(x, y, max_x, max_y):

    if x > 0:
        wor
        


def process(data):

    disks = {}
    max_x = 0
    max_y = 0

    for row in data:

        name, size, used, avail, usedperc = row.split()
        name_parts = name.split('-')
        name_x = int(name_parts[1][1:])
        name_y = int(name_parts[2][1:])

        if name_x > max_x:
            max_x = name_x

        if name_y > max_y:
            max_y = name_y

        name_string = "{},{}".format(name_x, name_y)
        disks[name_string] = (size, used, avail, usedperc)

    for idx_x in range(0, max_x + 1):
        for idx_y in range(0, max_y + 1):
            name_string = "{},{}".format(idx_x, idx_y)
            print disks[name_string]

            adj = get_adjacent(idx_x, idx_y, max_x, max_y)

    return disks



if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

results = process(data)

import ipdb; ipdb.set_trace()
print "Results: {}".format(results)
