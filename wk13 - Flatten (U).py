'''
Week 13 - Flatten
https://ejudge.it.kmitl.ac.th/problem/8343
'''

import json


def main():
    '''Main Function'''

    sequence = list(input())

    number_list = []

    number_holder = ''

    for char in sequence:
        if char.isnumeric():
            number_holder += char
            continue

        if number_holder:
            number_list.append(int(number_holder))
            number_holder = ''

    number_list.sort(reverse=True)

    print(number_list)


def main2():
    '''Main Function 2'''

    sequence = json.loads(input())

    number_list = []

    while len(sequence):
        sequence_length = len(sequence)

        for s in sequence:
            if not isinstance(s, list):
                