import math


def pathfinder(position, end):

    if(position == end):
        print('Destination Reached')

    else:

        run = end[0] - position[0]
        rise = end[1] - position[1]

        angle_rad = math.atan(run / rise)
        angle_deg = angle_rad * (180 / math.pi)

        # print('Current Position: ' + str(position))
        # print('Angle To End: ' + str(angle_deg))

        if 0 < angle_deg < 45:
            print('Moving Down 1')

            position[1] = position[1] + 1

            pathfinder(position, end)

        if 45 < angle_deg < 90:
            print('Moving Left 1')

            position[0] = position[0] + 1

            pathfinder(position, end)

        if angle_deg == 45:

            print('Moving Left and Down by 1')

            position[0] = position[0] + 1
            position[1] = position[1] + 1

            pathfinder(position, end)
        if angle_deg == 0:
            print('Moving y by 1')

            position[1] = position[1] + (end[1] - position[1])

            pathfinder(position, end)



map = [
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0],
]

start = -1
end = -1

for index, row in enumerate(map):

    for a, b in enumerate(row):

        if b == 1:
            start = [index, a]

        if b == 2:
            end = [index, a]


print('Start' + str(start))
print('End' + str(end))

pathfinder(start, end)
