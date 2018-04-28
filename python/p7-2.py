from collections import Counter
import sys
import os
import helpers
import re


def check(section):

    ret_val = []
    if len(section) < 3:
        return ret_val

    # print "Section: {}".format(section)
    # print section
    for idx in range(0, len(section) - 2):
        part = section[idx:idx+3]

        # print "{}{}".format(" "*idx, part)

        if part[0] == part[1]:
            continue

        if part[0] == part[2]:
            ret_val.append("{}{}{}".format(part[1], part[0], part[1]))

    return ret_val


def checkBAB(section, bab):

    if len(section) < 3:
        return False

    # print "Section: {}".format(section)
    for idx in range(0, len(section) - 2):
        part = section[idx:idx+3]
        #print part
        if part[0] == part[1]:
            continue

        if part[0:3] == bab:
            return True
            return "{}{}{}".format(part[1], part[0], part[1])

    return None


if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

count = 0
for row in data:

    parts = row.split('[')
    aba_parts = [s if ']' not in s else s.split(']')[-1] for s in parts]
    hypernet_parts = [s.split(']')[0] for s in parts if ']' in s]

    aba_parts_found = [check(part) for part in aba_parts]
    aba_parts_found = [i for sl in aba_parts_found for i in sl]

    found = False
    for aba in aba_parts_found:
        if found:
            break
        for h_part in hypernet_parts:
            if checkBAB(h_part, aba):
                count += 1
                found = True
                break

    if found:
        pass # print "{} supports SSL ({})".format(row, aba)
    else:
        print "{} does not support SSL".format(row)


print count


