'''
Week 11 - LastStand
https://ejudge.it.kmitl.ac.th/problem/8285
'''

import json


def main():
    '''Main Function'''

    array = json.loads(input())

    for i in array:
        print(str(i)[-1])


main()
