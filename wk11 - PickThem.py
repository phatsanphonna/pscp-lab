'''
Week 11 - PickThem
https://ejudge.it.kmitl.ac.th/problem/8283
'''

import json


def main():
    '''Main Function'''

    array = json.loads(input())

    number_list = []

    for number in array:
        if number % 2 == 0:
            number_list.append(number)

    if not number_list:
        print('Nope')
        return

    print(*number_list, sep='\n')


main()
