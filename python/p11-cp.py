# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque
from itertools import izip


keys = [1, 2, 3, 4]
short = {
    "polonium": "Po",
    "polonium-compatible": "Po",
    "thulium": "Tm",
    "thulium-compatible": "Tm",
    "promethium": "Pm",
    "promethium-compatible": "Pm",
    "ruthenium": "Ru",
    "ruthenium-compatible": "Ru",
    "cobalt": "Co",
    "cobalt-compatible": "Co",
    "hydrogen-compatible": "H",
    "hydrogen": "H",
    "lithium": "Li",
    "lithium-compatible": "Li",
}


def get_floors_copy(floors):
    ret = {}
    for fl in keys:
        if fl in floors:
            ret[fl] = list(floors[fl])

    return ret


def get_config_id(floors):
    h = ""
    for fl in keys:
        floor = list(floors[fl])
        floor.sort()
        h += str(fl) + "".join(floor)

    return h


def is_done(floors):

    for fl in [1, 2, 3]:
        if fl in floors:
            floor = floors[fl]
        else:
            continue

        if len(floor) > 0:
            return False

    return True


def is_safe_configuration(floors):

    for fl in keys:
        if fl in floors:
            floor = list(floors[fl])
        else:
            continue

        floor.sort()

        chips = [i for i in floor if i.endswith('M')]
        gens = [i for i in floor if i.endswith('G')]

        if len(gens) == 0:
            continue

        if len(chips) == 0:
            continue

        for idx in range(0, len(chips)):
            c = chips[idx]

            required_gen = c[0:-1] + 'G'

            # matching generator, remove it
            if required_gen not in gens:
                return False

    return True


def add_to_floor(floors, floor, kind, thing):

    if thing is not None and (thing[-1] == '.' or thing[-1] == ','):
        thing = thing[:-1]

    floor = floors[floor]

    if thing == 'generator':
        thing = short[kind] + "G"
    elif thing == 'microchip':
        thing = short[kind] + "M"

    floor.append(thing)


floor_names = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4
}


def generate_moves(depth, el, floors):

    state = (depth, el, floors)
    moves = []

    floor = floors[el]

    # all single ones
    for item in floor:
        if el < 4:
            moves.append((state, el + 1,  (item,)))
        if el > 1:
            moves.append((state, el - 1,  (item,)))

    # all pairs
    for idx, item in enumerate(floor):

        if idx == (len(floor) - 1):
            break
        remains = floor[idx+1:]
        pairs = zip([item] * len(remains), remains)

        for p in pairs:
            if el < 4:
                moves.append((state, el + 1,  p))
            if el > 1:
                moves.append((state, el - 1,  p))

    return moves


def make_move(floors, src, dest, items):

    fl = get_floors_copy(floors)
    fl[src] = [i for i in fl[src] if i not in items]
    fl[dest].extend(items)

    return fl


seen = set()


def search(original_floors):

    moves = deque()

    d = 1
    el = 1
    floors = original_floors



    new_moves = generate_moves(d, el, floors)
    moves.extendleft(new_moves)

    while len(moves):

        move = moves.pop()
        state, new_el, items = move
        depth, el, floors = state

        new_config = make_move(floors, el, new_el, items)

        h = get_config_id(new_config)
        if h in seen:
            continue

        seen.add(h)
        if not is_safe_configuration(new_config):
            continue

        if is_done(new_config):
            print "Done at {} moves".format(d)
            print floors
            sys.exit(2)

        moves.extendleft(generate_moves(depth + 1, new_el, new_config))


def process(data):

    floors = {
        1: [],
        2: [],
        3: [],
        4: []
    }

    for row in data:
        description = row.split()
        floor = floor_names.get(description[1])

        what = description[4:]

        if what[0] == "nothing":
            continue

        while True:
            if len(what) == 0:
                break

            if what[0] in ['and', 'a']:
                what = what[1:]

            add_to_floor(floors, floor, *(what[0:2]))

            what = what[3:]

    print floors

    search(floors)

    

if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

print "answer is {}".format(process(data))





