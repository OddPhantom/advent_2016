import sys
import os
import re


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


def check_triangle(sides):

    (side1, side2, side3) = sides

    calcs = [
        (side1 + side2) > side3,
        (side1 + side3) > side2,
        (side2 + side3) > side1
    ]

    if all(calcs):
        return True
    else:
        return False


def calculate_1(data):
    possible = 0

    for row in data:
        row = [int(r) for r in row.split()]

        if check_triangle(row):
            possible += 1

    return possible


def calculate_2(data):
    possible = 0

    t1 = [0, 0, 0]
    t2 = [0, 0, 0]
    t3 = [0, 0, 0]
    idx = 0
    for row in data:
        t1[idx], t2[idx], t3[idx] = [int(r) for r in row.split()]

        if idx == 2:
            for t in [t1, t2, t3]:
                if check_triangle(t):
                    possible += 1

        idx = (idx + 1) % 3                

    return possible


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
        answer = calculate_2(data)

    print "Answer is {}".format(answer)

    if expected_answer is not None:
        print "Expected answer is {}".format(expected_answer)

if __name__ == "__main__":
    main()

