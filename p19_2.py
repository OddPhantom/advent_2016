# -*- coding: utf-8 -*-
# from __future__ import division
import sys
import os
import helpers
from collections import deque
import hashlib
import binascii


#count = 12

count = 3001330


def get_across(idx, count):
    h = count // 2
    across = (idx + h) % count
    return across


def process():

    front = deque()
    back = deque()

    for i in range(1, count + 1):
        if i > count // 2:
            back.append(i)
        else:
            front.append(i)

    len_circle = count

    left = len(front) + len(back)
    #   print "front: {}".format(front)
    #print "back: {}".format(back)

    while left > 1:

        if left % 10000 == 0:
            print left

        elf_id = front.popleft()
        across_elf_id = back.popleft()

        back.append(elf_id)
        # adjust
        if len(back) - len(front) > 1:
            front.append(back.popleft())

        # print "stealing elf: {}".format(elf_id)
        # print "target elf: {}".format(across_elf_id)
        # print "front: {}".format(front)
        # print "back: {}".format(back)

        left = len(front) + len(back)


    print "front: {}".format(front)
    print "back: {}".format(back)


process()
