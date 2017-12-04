import sys
import os
import re
from collections import Counter

def read_file(filename):

    data = []
    expected_answer = None
    
    with file(filename) as fp:
        problem_part = fp.next().strip()

        for l in fp:
            if l != '\n':
                l = l
                data.append(l.strip())
            else:
                break

        try:
            answer = fp.next()
        except:
            answer = None

    if answer:
        expected_answer = answer.strip()

    return problem_part, data, expected_answer


base = ord('a')


def decode_name(name, sector_id):

    sentence = []
    for word in name:
        new_word = ""
        for letter in word:
            value = ord(letter) - base

            value = (value + sector_id) % 26

            new_word += chr(value + base)

        sentence.append(new_word)

    print "{} is sector {}".format(" ".join(sentence), sector_id)


def calculate_1(data):

    sector_sum = 0

    expected = None
    for row in data:

        room = row.split()

        if len(room) > 1:
            expected = room[1]

        room = room[0]

        name = room.split('-')

        sector_id = name[-1]
        name = name[:-1]
        
        name_chars = "".join(name)
        counts = Counter(name_chars)

        values = counts.items()

        values = sorted(values, key=lambda char_count: (-char_count[1], char_count[0]))

        calc_checksum = "".join([v[0] for v in values])

        if len(calc_checksum) > 5:
            calc_checksum = calc_checksum[0:5]

        sector_id, expected_checksum = sector_id.split('[')

        expected_checksum = expected_checksum[:-1]

        if expected_checksum == calc_checksum:
            # print "{} is real ".format(row)
            sector_sum += int(sector_id)

            #print name, sector_id

            decode_name(name, int(sector_id))

        else:
            # print "{} is decoy ".format(row)
            pass
        

    print "Sum of sector id is {}".format(sector_sum)


def main():

    if len(sys.argv) == 1:
        print "Pass filename"
        sys.exit(2)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print "Can't open {}".format(filename)
        sys.exit(2)

    problem_part, data, expected_answer = read_file(filename)

    if int(problem_part) == 1:
        answer = calculate_1(data)
    else:
        answer = calculate_1(data)

    print "Answer is {}".format(answer)

    if expected_answer is not None:
        print "Expected answer is {}".format(expected_answer)

if __name__ == "__main__":
    main()

