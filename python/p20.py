# -*- coding: utf-8 -*-
# from __future__ import division
import sys
import os
import helpers
from collections import deque
import hashlib
import binascii


def process(data):

    highest = 4294967295
    lowest = 0

    processed = []
    for row in data:

        parts = row.split("-")
        processed.append((int(parts[0]), int(parts[1])))

    processed.sort()

    if processed[0][0] != 0:
        return 0

    counter = 0
    idx = 0
    ip_count = 0

    while idx < len(processed):
        lower, upper = processed[idx]

        if counter < lower:
            ip_count += 1
            counter += 1
            counter

        if counter >= lower and counter <= upper:
            counter = upper + 1
            idx += 1
        elif counter > upper:
            idx += 1

    return ip_count


if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

print "answer: {}".format(process(data))

