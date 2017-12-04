# -*- coding: utf-8 -*-
import os
import sys
import helpers


class Screen(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = []
        self.empty = ' '
        self.clear()

    def clear(self):
        for r_idx in range(0, self.height):
            row = [self.empty] * self.width
            self.screen.append(row)

    def count(self):
        count = 0
        for r_idx in range(0, self.height):
            for c_idx in range(0, self.width):
                if self.screen[r_idx][c_idx] == '*':
                    count += 1
        return count

    def prnt(self):
        print "{}x{}".format(self.width, self.height)
        print '-' * self.width
        for idx in range(0, self.height):
            print "".join(self.screen[idx])
        print '-' * self.width + '\n'

    def get_row(self, row):
        if row >= 0 and row < self.height:
            return self.screen[row]
        else:
            return None

    def get_column(self, col):
        if col >= 0 and col < self.width:
            data = []
            for idx in range(0, self.height):
                data.append(self.screen[idx][col])
            return data
        else:
            return None

    def set_column(self, col, data):
        if col >= 0 and col < self.width:
            for idx in range(0, self.height):
                self.screen[idx][col] = data[idx]

    def set_row(self, row, data):
        if row >= 0 and row < self.height:
            self.screen[row] = data

    def valid_pixel(self, row, col):

        conditions = [
            row < self.height,
            row >= 0,
            col < self.width,
            col >= 0
        ]
        if all(conditions):
            return True

        return False

    def pixel_on(self, row, col):
        if self.valid_pixel(row, col):
            self.screen[row][col] = '*'

    def pixel_off(self, row, col):
        if self.valid_pixel(row, col):
            self.screen[row][col] = self.empty

    def rect(self, A, B):
        for idx_row in range(0, B):
            for idx_col in range(0, A):
                self.pixel_on(idx_row, idx_col)

    def rotate_row(self, row, steps):
        old_row = self.get_row(row)
        if old_row is None:
            return

        offset = self.width - (steps % self.width)

        new_end = old_row[:offset]
        new_front = old_row[offset:]
        new_row = new_front + new_end

        self.set_row(row, new_row)

    def rotate_col(self, col, steps):

        old_col = self.get_column(col)
        if old_col is None:
            return

        offset = self.height - (steps % self.height)

        new_bottom = old_col[:offset]
        new_top = old_col[offset:]
        new_col = new_top + new_bottom

        self.set_column(col, new_col)

    def rect_command(self, size):
        # print "rect {}".format(size)
        parts = size.split('x')
        self.rect(int(parts[0]), int(parts[1]))

    def rotate_command(self, kind, which, dummy, steps):
        # print "rotate {} {} {} {}".format(kind, which, dummy, steps)
        parts = which.split('=')
        if kind == 'row':
            row = int(parts[1])
            self.rotate_row(row, int(steps))
        elif kind == 'column':
            col = int(parts[1])
            parts = which.split('=')
            self.rotate_col(col, int(steps))
        else:
            print "what?"

    def process(self, data):

        dispatch = {
            'rect': self.rect_command,
            'rotate': self.rotate_command
        }

        for row in data:
            parts = row.split()
            dispatch[parts[0]](*parts[1:])

        self.prnt()


def test():
    s = Screen(7, 3)

    s.prnt()
    s.rect(3, 2)
    s.prnt()

    s.rotate_col(1, 1)
    s.prnt()
    s.rotate_row(0, 4)
    s.prnt()
    s.rotate_col(1, 1)
    s.prnt()

if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)


screen = Screen(50, 6)
screen.process(data)
print screen.count()
