from collections import Counter
import sys
import os
import helpers
import re


def check(section):

    if len(section) < 4:
        return False

    # print "Section: {}".format(section)
    for idx in range(0, len(section) - 3):
        part = section[idx:idx+4]
        #print part
        if part[0] == part[1]:
            continue

        if part[0] == part[3] and part[1] == part[2]:
            return True

    return False


if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)



def works_1(data):
    count = 0
    for row in data:

        parts = row.split('[')
        aba_parts = [s if ']' not in s else s.split(']')[-1] for s in parts]
        hypernet_parts = [s.split(']')[0] for s in parts if ']' in s]

        aba_parts_valid = [check(part) for part in aba_parts]
        hypernet_parts_valid = [check(part) for part in hypernet_parts]

        if any(aba_parts_valid) and not any(hypernet_parts_valid):
            # print "{} is TLS".format(row)
            count += 1
        else:
            pass  # print "{} Not TLS".format(row)

    print count

def works_2(data):

    count = 0
    for row in data:
        parts = re.split("[\[\]]", row)

        aba_parts = parts[::2]
        hypernet_parts = parts[1::2]

        aba_parts_valid = [check(part) for part in aba_parts]
        hypernet_parts_valid = [check(part) for part in hypernet_parts]

        if any(aba_parts_valid) and not any(hypernet_parts_valid):
            # print "{} is TLS".format(row)
            count += 1
        else:
            pass  # print "{} Not TLS".format(row)

    print count


def someone_else(data):

    import ipdb; ipdb.set_trace()
    def abba(x):
        return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))

    lines = [re.split(r'\[([^\]]+)\]', line) for line in data]
    parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
    print('Answer #1:', sum(abba(sn) and not(abba(hn)) for sn, hn in parts))
    print('Answer #2:', sum(any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))

works_1(data)
works_2(data)
someone_else(data)
