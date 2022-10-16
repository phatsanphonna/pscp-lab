'''
Week 9 - diamond
https://ejudge.it.kmitl.ac.th/problem/8253
'''


import math


def print_round(size, step: int):
    '''Print round'''

    for i in range(1, size+1, step):
        if i == 1:
            print(' ')
        print()


def main():
    '''Main Function'''

    size = int(input())

    half_size = math.floor(size)

    print_round()

