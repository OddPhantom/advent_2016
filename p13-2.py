# -*- coding: utf-8 -*-

import sys
import os
import helpers
from collections import deque

GREEN = '\033[92m'
PATH = '\033[91m'
TARGET = '\033[94m'
ENDC = '\033[0m'

# example
# fav_num = 10
# width = 10
# height = 10

# target_x = 7
# target_y = 4

# start_x = 1
# start_y = 1

# actual
fav_num = 1362
width = 45
height = 45

target_x = 49
target_y = 49

start_x = 1
start_y = 1


def calc(x, y):

    # x*x + 3*x + 2*x*y + y + y*y.

    val = x * x
    val += 3 * x
    val += 2 * x * y
    val += y
    val += y * y

    val += fav_num

    bval = "{0:015b}".format(val)

    count = 0

    for digit in list(bval):
        if digit == '1':
            count += 1

    if count % 2 == 0:
        # even,
        return '.'
    else:
        return "#"


def get_grid(max_x, max_y):

    grid = []

    for y in range(0, max_x):
        row = []
        for x in range(0, max_y):
            row.append(calc(x, y))
        grid.append(row)

    return grid


def print_grid(grid, target_x, target_y, path=None):

    max_y = len(grid)
    max_x = len(grid[0])

    # top row

    nums = [list("{0:2}".format(x)) for x in range(0, max_x)]
    nums = zip(*nums)

    for n in nums:
        sys.stdout.write("   " + "".join(n))
        sys.stdout.write('\n')

    for y in range(0, max_y):
        sys.stdout.write("{0: 2} ".format(y))
        for x in range(0, max_x):
            if path is not None and (x, y) in path:
                sys.stdout.write(PATH)
                sys.stdout.write('O')
                sys.stdout.write(ENDC)
            else:
                if x == target_x and y == target_y:
                    sys.stdout.write(TARGET)
                sys.stdout.write(grid[y][x])
                if x == target_x and y == target_y:
                    sys.stdout.write(ENDC)

        sys.stdout.write('\n')


def get_moves(grid, path):

    x, y = path[-1]

    open_list = []
    for mod_x, mod_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

        new_x = x + mod_x
        new_y = y + mod_y
        if new_x < 0 or new_y < 0:
            continue

        if new_x >= width or new_y >= height:
            continue

        if grid[new_y][new_x] == '.':
            new_path = list(path)
            new_path.append((new_x, new_y))
            open_list.append(new_path)

    return open_list


def find_path(grid, x, y, t_x, t_y):

    open_list = deque()

    first_move = [(x, y)]
    open_list.append(first_move)

    seen = set()
    fifty = set()

    while len(open_list):

        path = open_list.pop()
        current = path[-1]
        if current in seen:
            continue
        seen.add(current)

        if (len(path) - 1) <= 50:
            fifty.add(current)

        if current[0] == t_x and current[1] == t_y:
            print_grid(grid, target_x, target_y, path)
            print "Got to cell in {} steps".format(len(path) - 1)
            print "\n"

            sys.exit(0)

        new_paths = get_moves(grid, path)

        open_list.extendleft(new_paths)

    print "Got to {} cells in at most fifty steps".format(len(fifty))


grid = get_grid(width, height)
steps = find_path(grid, start_x, start_y, target_x, target_y)
print_grid(grid, target_x, target_y)
