# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque
import hashlib
import binascii


starting_position = (0, 0)
puzzle_input = "udskfozm"


MAX_POS_Y = 4
MAX_POS_X = 4

goal_pos = [3, 3]


def what_is_open(path):

    hash_input = puzzle_input + "".join(path)
    m = hashlib.md5()
    m.update(hash_input)
    hash_output = m.digest()
    hex_output = binascii.hexlify(hash_output)

    doors = list(hex_output)[0:4]

    door_status = [True if door in ['b', 'c', 'd', 'e', 'f'] else False for door in doors]

    return door_status


directions = ('U', 'D', 'L', 'R')


vectors = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}



def get_moves(position, path):

    doors = what_is_open(path)
    possible = zip(doors, directions)
    moves = [m[1] if m[0] else None for m in possible]

    new_moves = []

    for d in moves:
        if d is None:
            continue

        new_pos = [None, None]
        v = vectors[d]
        new_pos[0] = position[0] + v[0]
        new_pos[1] = position[1] + v[1]

        conditions = [
            new_pos[0] >= 0,
            new_pos[1] >= 0,
            new_pos[0] < MAX_POS_X,
            new_pos[1] < MAX_POS_Y,
        ]

        if all(conditions):

            new_path = list(path)
            new_path.append(d)
            new_moves.append((new_pos, new_path))

    return new_moves


def process():
    q = deque()
    moves = get_moves(starting_position, [])
    q.extend(moves)
    print puzzle_input

    paths = []

    while len(q) > 0:
        pos, path = q.pop()
        # print "".join(path)
        # print pos

        if pos == goal_pos:
            #print len(paths)
            paths.append("".join(path))
            continue
        
            #print "path: {}".format("".join(path))

        moves = get_moves(pos, path)
        q.extend(moves)

    import ipdb; ipdb.set_trace()
    paths = [len(x) for x in paths]
    paths.sort()
    print paths[-1]

process()        
