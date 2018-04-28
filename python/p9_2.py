# -*- coding: utf-8 -*-
# time to run:
# python p9_2.py p9-1.txt  2000.72s user 6.09s system 99% cpu 33:32.81 total

import os
import sys
import helpers

COMPRESSION_COMMAND = 10
COMPRESSION_READ_DATA = 20


def process(depth, data):

    command = None
    state = None
    total_count = 0
    repeat = count = 0
    repeat_data = ""

    for c in data:

        if state is None:
            if c == '(':
                state = COMPRESSION_COMMAND
                command = ""
            else:
                total_count += 1

        elif state == COMPRESSION_COMMAND:
            if c == ')':
                state = COMPRESSION_READ_DATA
                count, repeat = [int(x) for x in command.split('x')]
                repeat_data = ""
            else:
                command += c

        elif state == COMPRESSION_READ_DATA:

            repeat_data += c
            count -= 1

            # do repeat into output
            if count == 0:
                expanded = repeat_data * repeat
                total_count += process(depth + 1, expanded)
                state = None
                repeat_data = ""

    return total_count


if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)


print "total count is {}".format(process(0, data[0]))
