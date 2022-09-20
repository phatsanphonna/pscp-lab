'''
<Recommend>
Week 9 - Cha Cha Cha
'''

import math


def main():
    '''Main Function'''

    days = int(input())

    total_hours = 0

    for _ in range(days):
        hours = math.ceil(float(input()))

        total_hours += hours

    print(8720 * total_hours)


main()
