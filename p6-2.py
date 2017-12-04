from collections import Counter
import sys
import os
import helpers

if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

counters = [Counter() for c in range(0, len(data[0]))]

for row in data:
    for idx, c in enumerate(list(row)):
        counters[idx][c] += 1


c1 = [c.most_common()[-1][0] for c in counters]

print "".join(c1)
