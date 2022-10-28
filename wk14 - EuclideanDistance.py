'''
Week 14 - EuclideanDistance
https://ejudge.it.kmitl.ac.th/problem/8393
'''


import math


def main():
    '''Main Function'''

    total_point = int(input())

    x_pos, y_pos = 0, 0

    total_distance = 0

    for i in range(total_point):
        pos = input().split(' ')

        pos[0] = float(pos[0])
        pos[1] = float(pos[1])

        if i == 0:
            x_pos = pos[0]
            y_pos = pos[1]
            continue

        total_distance += math.sqrt((pos[0] - x_pos)**2 + (pos[1] - y_pos)**2)
        x_pos, y_pos = pos[0], pos[1]

    print('%.2f' % total_distance)


main()
