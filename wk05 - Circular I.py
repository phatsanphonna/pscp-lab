'''Week 5 - Circular I'''

import math


def main():
    '''Main Function'''

    machine_x_pos = float(input())
    machine_y_pos = float(input())
    machine_radius = float(input())
    mosquito_x_pos = float(input())
    mosquito_y_pos = float(input())

    distance_between_mosquito = math.sqrt(
        (mosquito_x_pos - machine_x_pos)**2 + (mosquito_y_pos - machine_y_pos)**2)

    if distance_between_mosquito <= machine_radius:
        print('Yes')
    else:
        print('No')


main()
