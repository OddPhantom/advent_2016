# -*- coding: utf-8 -*-

import os
import sys
import helpers

COMPRESSION_COMMAND = 'command'
COMPRESSION_READ_DATA = 'data'


def process(data):

    command = None
    state = None

    repeat = count = 0
    repeat_data = ""

    with file('p9.out', 'w') as fp:
        import ipdb; ipdb.set_trace()
        for c in data:
            if state is None:
                if c == '(':
                    state = COMPRESSION_COMMAND
                    command = ""
                else:
                    fp.write(c)

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
                    while repeat > 0:
                        fp.write(repeat_data)
                        repeat -= 1
                    state = None


if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

process(data[0])
