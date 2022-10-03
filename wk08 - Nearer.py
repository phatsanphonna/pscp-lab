'''
Week 8 - Nearer
https://ejudge.it.kmitl.ac.th/problem/8232
'''


def main():
    '''Main Function'''

    alice_pos = int(input())
    bob_pos = int(input())
    ice_cream_car_pos = int(input())

    alice_distance = 0
    bob_distance = 0

    alice_distance = abs(alice_pos - ice_cream_car_pos)

    bob_distance = abs(bob_pos - ice_cream_car_pos)

    if bob_distance > alice_distance:
        print('Alice %d' % alice_distance)
    elif bob_distance < alice_distance:
        print('Bob %d' % bob_distance)
    else:
        print('Sundaes %d' % alice_distance)


main()
