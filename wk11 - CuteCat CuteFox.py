'''
Week 11 - CuteCat CuteFox
https://ejudge.it.kmitl.ac.th/problem/8296
'''

import json


def main():
    '''Main Function'''

    total = int(input())

    total_cat = 0
    cat_list = []

    total_fox = 0
    fox_list = []

    fox = dict().items()
    for _ in range(total):
        raw_data = input()
        data = json.loads(raw_data)

        key = list(data.keys())[0]
        print(data[key])


main()
