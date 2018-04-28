# -*- coding: utf-8 -*-
# from __future__ import division
import sys
import os
import helpers
from collections import deque
import hashlib
import binascii


count = 12

# count = 3001330

presents = {}
circle = range(1, count + 1)

for i in circle:
    presents[i] = 1


def get_across(idx, count):
    h = count // 2
    across = (idx + h) % count
    return across


def process():

    len_circle = count
    circle_idx = 0

    import ipdb; ipdb.set_trace()
    while len_circle > 1:
        if len_circle % 10000 == 0:
            print len_circle

        elf_id = circle[circle_idx]
        
        across_idx = get_across(circle_idx, len(circle))
        elf_across_id = circle[across_idx]


        print "circle: {}".format(circle)
        #        print "presents: {}".format(presents)
        print "circle_idx: {}".format(circle_idx)
        print "elf id: {}".format(elf_id)
        print "across_idx: {}".format(across_idx)        
        print "across elf id: {}".format(elf_across_id)
 


        del circle[across_idx]
        presents[elf_id] += presents[elf_across_id]
        del presents[elf_across_id]

        len_circle -= 1

        circle_idx += 1

        if circle_idx >= len_circle:
            circle_idx = 0


    print presents


process()

    
