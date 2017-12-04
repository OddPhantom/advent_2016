
import json
import sys

steps = "R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3"
#steps = " L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"
#steps = "R2, L3"
#steps = "R2, R2, R2"
#steps = "R5, L5, R5, R3"
#steps = "R8, R4, R4, R8"

steps = steps.replace(" ", "")
steps = steps.split(',')

location = [0, 0]

v = [0, 1]

spots = set()
first_dup = None

spots.add(json.dumps(location))

for step in steps:

    d = step[0]
    l = int(step[1:])

    if d == 'L':
        v = [(-1 * v[1]), v[0]]
    else:
        v = [v[1], (-1 * v[0])]

    location_x = location[0] + (v[0] * l)
    location_y = location[1] + (v[1] * l)

    if first_dup is None:
        visit = [location[0], location[1]]
        for delta in range(1, l+1):
            visit = [visit[0] + v[0], visit[1] + v[1]]
            v_string = json.dumps(visit)
            if v_string in spots:
                print "Already been at {}".format(visit)
                first_dup = visit
            else:
                spots.add(v_string)

    location = [location_x, location_y]
    print "with {}, now facing {}, moved to {} ".format(step, v, location)

    goal = location


# [-23, -11]

print goal
print abs(goal[0]) + abs(goal[1])

print "should be at {}".format(first_dup)

print "really need to be at {}".format(first_dup)
print abs(first_dup[0]) + abs(first_dup[1])

