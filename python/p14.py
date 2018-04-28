# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque
import hashlib
import binascii

salt = "qzyelonm"
#salt = "abc"

idx = 0

keys_found = []


seen = dict()


def make_hash_input(idx):
    return "{}{}".format(salt, idx)


def same_as(items, desired):
    return all(x == desired for x in items)


def all_same(items):
    return all(x == items[0] for x in items)


def do_hash(hash_input):

    m = hashlib.md5()
    m.update(hash_input)
    hash_output = m.digest()
    hash_input = binascii.hexlify(hash_output)

    count = 0
    while count < 2016:
        m = hashlib.md5()
        m.update(hash_input)
        hash_output = m.digest()
        hash_input = binascii.hexlify(hash_output)

        count += 1

    return hash_input


def check_if_key(k_idx, found_triple):

    for l_idx in range(1, 1001):
        hash_idx = k_idx + l_idx

        if hash_idx in seen:
            text = seen[hash_idx]
        else:
            hash_input = make_hash_input(hash_idx)
            text = do_hash(hash_input)
            seen[hash_idx] = text

        quints = zip(text, text[1:], text[2:], text[3:], text[4:])

        if any([same_as(item, found_triple) for item in quints]):
            return True

    return False


while len(keys_found) < 64:

    hash_input = make_hash_input(idx)

    five = None
    text = None

    if idx in seen:
        text = seen[idx]
    else:
        text = do_hash(hash_input)
        seen[idx] = text

    triples_list = zip(text, text[1:], text[2:])
    found_triples = [triple[0] for triple in triples_list if all_same(triple)]

    if len(found_triples) > 0:
        # could be key
        # sys.stdout.write("{}".format(idx))

        if check_if_key(idx, found_triples[0]):
            keys_found.append(text)
            sys.stdout.write("{}".format(idx))
            sys.stdout.write(".")

    else:
        if idx not in seen:
            seen[idx] = (False, text)

    sys.stdout.flush()

    if len(keys_found) == 64:
        print "Index {} is key 64".format(idx)
        print "{}".format(text)
    idx += 1


