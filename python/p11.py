# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque
from itertools import izip


keys = [1, 2, 3, 4]
short = {
    "elerium": "El",
    "elerium-compatible": "El",
    "dilithium": "Di",
    "dilithium-compatible": "Di",
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


def mprint(str):

    pass


def get_floors_copy(floors):
    ret = {}
    for fl in keys:
        if fl in floors:
            ret[fl] = list(floors[fl])

    return ret


def get_config_id(el, floors):
    """ Returns a string to represent the elevator position and the configuration
    of the items on each floor
    """
    h = "{}:".format(el)
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


def get_floor_string(floors):
    ret = ""

    for k in keys:
        fl = floors[k]
        ret += "{}: {}".format(k, ",".join(fl))
        ret += " "

    return ret


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
            chip = chips[idx]

            required_gen = chip[0:-1] + 'G'

            if required_gen not in gens:
                mprint("Floor {} not valid {}, missing {} for {}".format(fl,
                                                                         get_floor_string(floors),
                                                                         required_gen,
                                                                         chip))
                return False

    mprint("Floor valid {}".format(get_floor_string(floors)))
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

    moves = []

    floor = floors[el]
    mprint("\nFor {}, eleveator on {}".format(get_floor_string(floors), el))
    mprint("Possible Moves are :")

    # all single ones
    for item in floor:
        if el < 4:
            new_config = make_move(floors, el, el + 1, (item,))
            mprint("\t{0: <15} to {1}\t {2}".format(item, el + 1, get_floor_string(new_config)))
            moves.append((depth, el + 1, new_config))
        if el > 1:
            new_config = make_move(floors, el, el - 1, (item,))
            mprint("\t{0: <15} to {1}\t {2}".format(item, el - 1, get_floor_string(new_config)))
            moves.append((depth, el - 1, new_config))

    # all pairs
    for idx, item in enumerate(floor):

        if idx == (len(floor) - 1):
            break
        remains = floor[idx+1:]
        pairs = zip([item] * len(remains), remains)

        for p in pairs:
            if el < 4:
                new_config = make_move(floors, el, el + 1, p)
                mprint("\t{0: <15} to {1}\t {2}".format(p, el + 1, get_floor_string(new_config)))
                moves.append((depth, el + 1, new_config))
            if el > 1:
                new_config = make_move(floors, el, el - 1, p)
                mprint("\t{0: <15} to {1}\t {2}".format(p, el - 1, get_floor_string(new_config)))
                moves.append((depth, el - 1, new_config))

    return moves


def make_move(floors, src, dest, items):

    fl = get_floors_copy(floors)
    fl[src] = [i for i in fl[src] if i not in items]
    fl[dest].extend(items)
    fl[dest].sort()

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

        depth, el, floors = moves.pop()

        h = get_config_id(el, floors)
        if h in seen:
            continue

        seen.add(h)
        if not is_safe_configuration(floors):
            continue

        if is_done(floors):
            print "Done at {} moves".format(depth)
            print floors
            sys.exit(2)

        moves.extendleft(generate_moves(depth + 1, el, floors))


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





