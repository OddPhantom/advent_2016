

import sys
import os


def read_file(filename):

    data = []

    with file(filename) as fp:
        button_type = fp.next().strip()

        for l in fp:
            if l != '\n':
                data.append(l.strip())
            else:
                break

        try:
            answer = fp.next()
        except:
            answer = None

    if answer:
        answer = answer.strip()

    return button_type, data, answer


class ButtonPad(object):

    def __init__(self, *args, **kwargs):
        self._row = 1
        self._column = 1
        self.max_rc = 2

        self.pad = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
        ]

    def can_go(self, row, column):
        conditions = [row < 0,
                      column < 0,
                      row > self.max_rc,
                      column > self.max_rc]

        if any(conditions):
            return False
        if self.pad[row][column] is not None:
            return True
        return False

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        if self.can_go(value, self.column):
            self._row = value

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, value):
        if self.can_go(self.row, value):
            self._column = value

    def get_number(self):
        return self.pad[self.row][self.column]

    def move(self, direction):

        if direction == 'U':
            self.row -= 1
        elif direction == 'D':
            self.row += 1
        elif direction == 'L':
            self.column -= 1
        elif direction == 'R':
            self.column += 1


class ButtonPad2(ButtonPad):

    def __init__(self, *args, **kwargs):
        self._row = 2
        self._column = 0
        self.max_rc = 4

        self.pad = [
            [None, None, "1", None, None],
            [None, "2", "3", "4", None],
            ["5",  "6",  "7",  "8",  "9"],
            [None, "A", "B", "C", None],
            [None, None, "D", None, None]
        ]


def calculate(button_type, data):
    if button_type == "1":
        b = ButtonPad()
    elif button_type == "2":
        b = ButtonPad2()

    sequence = []
    for row in data:
        for step in row:
            b.move(step)
        sequence.append(b.get_number())

    return "".join([str(s) for s in sequence])


def main():

    if len(sys.argv) == 1:
        print "Pass filename"
        sys.exit(2)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print "Can't open {}".format(filename)
        sys.exit(2)

    pad, data, expected_answer = read_file(filename)

    answer = calculate(pad, data)
    print "Answer is {}".format(answer)

    if expected_answer is not None:
        print "Expected answer is {}".format(expected_answer)

if __name__ == "__main__":
    main()


