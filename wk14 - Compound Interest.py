'''
Week 14 - Compound Interest
https://ejudge.it.kmitl.ac.th/problem/8399
'''


def main():
    '''Main Function'''

    money = int(input())
    interest = float(input()) / 100
    years = int(input())

    total = money

    for _ in range(years):
        total += total * interest

    print('%.2f' % total)


main()
