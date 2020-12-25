import math


def pathfinder(position, end):

    if(position == end):
        print('Destination Reached')

    else:

        run = end[0] - position[0]
        rise = end[1] - position[1]

        angle_rad = math.atan(run / rise) # Using tangent trig ratio to find angle in radians
        angle_deg = angle_rad * (180 / math.pi) # Converting radians to degrees. Primarily for aesthetics.

        print('Current Position: ' + str(position))
        print('Angle To End: ' + str(angle_deg))

        if 0 < angle_deg < 45:

            if rise > 0:
                position[1] = position[1] + 1
                print('Moving Down 1')
            if rise < 0:
                position[1] = position[1] - 1
                print('Moving Up 1')

            pathfinder(position, end)

        if 45 < angle_deg < 90:

            if run > 0:
                position[0] = position[0] + 1
                print('Moving Left 1')
            if run < 0:
                position[0] = position[0] - 1
                print('Moving Right 1')

            pathfinder(position, end)

        if angle_deg == 45:

            if rise > 0:
                x = 'Down'
                position[1] = position[1] + 1
            if rise < 0:
                x = 'Up'
                position[1] = position[1] - 1

            if run > 0:
                y = 'Right'
                position[0] = position[0] + 1
            if run < 0:
                y = 'Left'
                position[0] = position[0] - 1

            print(x + y)
            pathfinder(position, end)

        if angle_deg == -45:

            if rise > 0:
                x = 'Down'
                position[1] = position[1] + 1
            if rise < 0:
                x = 'Up'
                position[1] = position[1] - 1

            if run > 0:
                y = 'Right'
                position[0] = position[0] + 1
            if run < 0:
                y = 'Left'
                position[0] = position[0] - 1

            print(x + y)
            pathfinder(position, end)

        if angle_deg == 0:
            print('Moving y by 1')

            position[1] = position[1] + (end[1] - position[1])

            pathfinder(position, end)

        if -45 < angle_deg < 0:

            if rise > 0:
                position[1] = position[1] + 1
                print('Moving Down 1')
            if rise < 0:
                position[1] = position[1] - 1
                print('Moving Up 1')

            pathfinder(position, end)

        if -90 < angle_deg < -45:

            if run > 0:
                position[1] = position[1] + 1
                print('Moving Down 1')
            if run < 0:
                position[1] = position[1] - 1
                print('Moving Up 1')

            pathfinder(position, end)


map = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
]

start = -1
end = -1
walls = []  # Wall functionality will be added later on

# Finding start and end coordinates in the entire array.
for index, row in enumerate(map):

    for a, b in enumerate(row):

        if b == 1:
            start = [a, index]

        if b == 2:
            end = [a, index]

        if b == 3:
            walls.append(index, a)

if start == -1 or end == -1:
    print('Your start (1) or finish (2) are missing from the map')

else:
    print('Start' + str(start))
    print('End' + str(end))

    pathfinder(start, end)
