'''Week 4 - PointInCircle'''


import math


def main():
    '''Main Function'''

    x_pos = float(input())
    y_pos = float(input())
    radius = float(input())
    xn_pos = float(input())
    yn_pos = float(input())

    distance = math.sqrt(
        (xn_pos - x_pos)**2 + (yn_pos - y_pos)**2)

    print(distance <= radius)


main()
