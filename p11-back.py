# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import defaultdict


floors = {}


def get_floor(floor):
    if floor not in floors:
        floors[floor] = Floor(floor)
    return floors[floor]


class Elevator(object):

    def __init__(self):
        self.floor = 1
        self.items = [None, None]

    def load(self, item):
        loaded = False

        for idx, item in enumerate(self.items):
            if item is None:
                self.items[idx]
                loaded = True
                break

        return loaded

    def unload(self, idx):
        item = self.items[idx]
        self.items[idx] = None
        return item

class Floor(object):

    def __init__(self, name):
        self.name = name
        self.items = []

    def __repr__(self):
        return "Floor {} has {}".format(self.name,
                                        [str(item) for item in self.items])

    def add(self, item):
        if item is None:
            return
        self.items.append(item)

    def can_have_on_floor(self, item):
        if len(self.items) == 0:
            return True

        generators = [i.kind for i in self.items if i.is_generator()]

        if item.is_chip():

            # can be here if there are no generators
            if len(generators) == 0:
                return True

            # or it' s matching generator is here
            g_k = [i for i in generators if i.kind == item.kind]
            if len(g_k) > 0:
                return True

            return False
        else:
            # can put the generator here if there are no chips
            chips = set([i.kind for i in self.items if i.is_chip()])
            if len(chips) == 0:
                return True

            generators = set([i.kind for i in self.items if i.is_generator()])

            # or if there's one chip here that's of the kind
            # and there are not chips without their generator
            unmatched_chips = chips - generators
            if len(unmatched_chips) > 0 and item.kind in chips:
                return True

            return False

        

class Chip(object):

    def __init__(self, kind):
        self.kind = kind

    def safe(self, item):
        if isinstance(item, Chip):
            return True

    def is_chip(self):
        return True

    def is_generator(self):
        return False

    def __repr__(self):
        return "{} chip".format(self.kind)


class Generator(object):
    def __init__(self, kind):
        self.kind = kind

    def is_chip(self):
        return False

    def is_generator(self):
        return True
        
    def __repr__(self):
        return "{} generator".format(self.kind)

    def safe(self, item):
        if isinstance(item, Generator):
            return True


def add_to_floor(floor, kind, thing):

    if thing is not None and (thing[-1] == '.' or thing[-1] == ','):
        thing = thing[:-1]

    floor = get_floor(floor)

    if thing == 'generator':
        thing = Generator(kind)
    elif thing == 'microchip':
        thing = Chip(kind)

    floor.add(thing)


floor_names = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4
}


def process(data):

    for row in data:
        description = row.split()
        floor = floor_names.get(description[1])

        what = description[4:]

        if what[0] == "nothing":
            add_to_floor(floor, None, None)
            continue

        while True:
            if len(what) == 0:
                break

            if what[0] in ['and', 'a']:
                what = what[1:]

            add_to_floor(floor, *(what[0:2]))

            what = what[3:]

    # move stuff.
    # 


if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

print "answer is {}".format(process(data))


fl = floors.values()
fl.sort(key=lambda x: x.name, reverse=True)

for f in fl:
    print f
