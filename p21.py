# -*- coding: utf-8 -*-
# from __future__ import division
import sys
import os
import helpers
from collections import deque
import hashlib
import binascii


def swap_letter(password, *args):
    """swap letter X with letter Y
    means that the letters X and Y should be swapped
    (regardless of where they appear in the string)."""
    x_arg = args[0]
    y_arg = args[3]
    x = password.index(x_arg)
    y = password.index(y_arg)

    t = password[x]
    password[x] = password[y]
    password[y] = t

    return password


def swap_position(password, *args):
    """ swap position X with position Y
    means that the letters at indexes X and Y
    (counting from 0) should be swapped."""

    x = int(args[0])
    y = int(args[3])

    t = password[x]
    password[x] = password[y]
    password[y] = t

    return password


def rotate_left(password, *args):
    """rotate left/right X steps
    means that the whole string should be rotated;
    for example, one right rotation would turn abcd into dabc."""

    steps = int(args[0])
    pwd = deque(password)
    
    while steps > 0:
        val = pwd.popleft()
        pwd.append(val)
        steps -= 1
        
    return list(pwd)


def rotate_right(password, *args):
    """rotate left/right X steps
    means that the whole string should be rotated;
    for example, one right rotation would turn abcd into dabc."""
    steps = int(args[0])
    pwd = deque(password)
    
    while steps > 0:
        val = pwd.pop()
        pwd.appendleft(val)
        steps -= 1
        
    return list(pwd)

def rotate_based(password, *args):
    """rotate based on position of letter X
    means that the whole string
    should be rotated to the right based on the index of letter X
    (counting from 0) as determined before this instruction does any
    rotations.  Once the index is determined, rotate the string to the
    right one time, plus a number of times equal to that index, plus
    one additional time if the index was at least 4.

    """
    letter = args[4]
    l_idx = password.index(letter)
    steps = 1 + l_idx
    if l_idx >= 4:
        steps += 1

    return rotate_right(password, steps, "dummy")


def reverse_positions(password, *args):
    """ reverse positions X through Y
    means that the span of letters at
    indexes X through Y (including the letters at X and Y) should be
    reversed in order."""

    x = int(args[0])
    y = int(args[2])

    sub = password[x:y+1]
    sub.reverse()
    
    for idx, pwd_idx in enumerate(range(x, y+1)):
        password[pwd_idx] = sub[idx]
        
    return password


def move_position(password, *args):
    """move position X to position Y
    means that the letter which is at
    index X should be removed from the string, then inserted such that it
    ends up at index Y."""
    x = int(args[0])
    y = int(args[3])

    x_val = password[x]
    del password[x]
    password.insert(y, x_val)
        
    return password


funcs = {
    "swap_letter": swap_letter,
    "swap_position": swap_position,
    "rotate_left": rotate_left,
    "rotate_right": rotate_right,
    "rotate_based": rotate_based,
    "reverse_positions": reverse_positions,
    "move_position": move_position
}


def process(password, data):

    password = list(password)
    for row in data:
        parts = row.split()

        func = funcs.get("{}_{}".format(parts[0], parts[1]))

        old_password = "".join(password)
        password = func(password, *parts[2:])
        print "after {} password {} is {}".format(row,
                                               old_password,
                                               "".join(password))

    return "".join(password)


initial_pwd = "abcdefgh"

if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

print "answer: {}".format(process(initial_pwd, data))

