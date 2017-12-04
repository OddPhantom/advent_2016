# -*- coding: utf-8 -*-
import sys
import os
import helpers

bots = {}
output = {}


def get_bot(num):

    if num not in bots:
        bots[num] = Bot(num)

    return bots[num]


def get_output(num):
    if num not in output:
        output[num] = Output(num)

    return output[num]


class Output(object):
    def __init__(self, num):
        self.num = num
        self._value = None

    def name(self):
        return "Output {}".format(self.num)

    def __repr__(self):
        return u"Output {} with value {}".format(self.num, self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_in):
        self._value = value_in


class Bot(object):
    desired = [17, 61]

    def __init__(self, num):
        self.num = num
        self._high = None
        self._low = None
        self._value = []

    def name(self):
        return "Bot {}".format(self.num)

    def __repr__(self):
        return u"Bot {} with value {}".format(self.num, self.value)

    def maybe_give(self):

        for d in self.desired:
            if d in self._value:
                print "{} has {} ({})".format(self.name(), d, self._value)

        if len(self._value) != 2:
            return

        self._value.sort()

        if self.desired == self._value:
            print "Bot {} will compare {}".format(self.num, self.desired)

        if self.low is None or self.high is None:
            return
        min_val = min(self._value)
        max_val = max(self.value)
        m = ("{} has 2 microchips, "
             "it gives value-{} to {} "
             "and value-{} to {}".format(self.name(),
                                         min_val,
                                         self.low.name(),
                                         max_val,
                                         self.high.name()))
        # print m
        self.low.value = min_val
        self.high.value = max_val
        
        self._value = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_in):
        if value_in in self.desired:
            print "bot {} got {}".format(self.num, value_in)
        self._value.append(value_in)
        self.maybe_give()

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        self._low = value
        self.maybe_give()

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        self._high = value
        self.maybe_give()

    def setup(self, which, d2, who_type, who_id):
        if who_type == 'bot':
            who = get_bot(who_id)
        else:
            who = get_output(who_id)
        if which == 'low':
            self.low = who
        elif which == 'high':
            self.high = who


def process(data):
    for row in data:
        ins = row.split()

        if ins[0] == 'value':
            bot = get_bot(ins[-1])
            bot.value = int(ins[1])

        if ins[0] == 'bot':

            bot = get_bot(ins[1])

            args = ins[3:3+4]
            bot.setup(*args)
            args = ins[8:]
            bot.setup(*args)


if len(sys.argv) == 1:
    print "Pass filename"
    sys.exit(2)

filename = sys.argv[1]
if not os.path.exists(filename):
    print "Can't open {}".format(filename)
    sys.exit(2)

data = helpers.read_file(filename)

print "answer is {}".format(process(data))

for k, v in output.items():
    print v
