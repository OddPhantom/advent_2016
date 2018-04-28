# -*- coding: utf-8 -*-
import sys
import os
import helpers

reg = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}



def process(data):

    ip = 0
    last = len(data)

    while ip < len(data):
        row = data[ip]
        parts = row.split()
        ins = parts[0]

        if ins == 'cpy':
            val = parts[1]
            if val not in reg.keys():
                reg[parts[2]] = int(parts[1])
            else:
                reg[parts[2]] = reg[parts[1]]
            ip += 1
        elif ins == 'inc':
            reg[parts[1]] += 1
            ip += 1
        elif ins == 'dec':
            reg[parts[1]] -= 1
            ip += 1

        elif ins == 'jnz':

            val = parts[1]
            if val in reg.keys():
                t = reg[parts[1]] != 0
            else:
                val = int(val)
                t = (val != 0)
                
            if t:
                ip = ip + int(parts[2])
            else:
                ip += 1



if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

process(data)


print "register a has {}".format(reg['a'])


