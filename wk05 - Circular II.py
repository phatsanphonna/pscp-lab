'''Week 5 - Circular II'''

import math


def main():
    '''Main Function'''

    machine1_x_pos = float(input())
    machine1_y_pos = float(input())
    machine1_radius = float(input())

    machine2_x_pos = float(input())
    machine2_y_pos = float(input())
    machine2_radius = float(input())

    distance_between_machine = math.sqrt(
        (machine2_x_pos - machine1_x_pos)**2
        + (machine2_y_pos - machine1_y_pos)**2
    )

    total_radius = machine1_radius + machine2_radius

    if distance_between_machine < total_radius:
        print('Yes')
    else:
        print('No')


main()
