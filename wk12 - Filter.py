'''
Week 12 - Filter
https://ejudge.it.kmitl.ac.th/problem/8322
'''


import json


def main():
    '''Main Function'''

    data = json.loads(input())
    final_score = float(input())

    final_data = []

    for key in data:
        if float(data[key]) >= final_score:
            final_data.append('%s\t%.2f' % (key, float(data[key])))

    if not final_data:
        print('Nope')
        return

    final_data = sorted(final_data)

    print(*final_data, sep='\n')


main()
