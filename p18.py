# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque
import hashlib
import binascii


starting_row = "ABCDE"

SAFE = '.'
TRAP = '^'

def get_parents(idx, parent_row):

    p = idx - 1
    n = idx + 1

    parents = [SAFE, SAFE, SAFE]
    if p >= 0:
        parents[0] = parent_row[p]

    parents[1] = parent_row[idx]

    if n < len(parent_row):
        parents[2] = parent_row[n]

    return parents


def is_trapped(val):

    if val in[[TRAP, TRAP, SAFE],
              [SAFE, TRAP, TRAP],
              [TRAP, SAFE, SAFE],
              [SAFE, SAFE, TRAP]]:
        return TRAP

    return SAFE


def process(row, rows_needed):

    count = 1
    safe = 0
    while True:

        # print "".join(row)
        safe += len([x for x in row if x == SAFE])

        if count >= rows_needed:
            break

        next_row = [get_parents(idx, row) for idx in range(0, len(row))]
        row = [is_trapped(p) for p in next_row]
        count += 1

    print "safe {}".format(safe)



s = ".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^."
process(s, 40)
process(s, 400000)

# example
#s = ".^^.^.^^^^"
#process(s, 10)
