'''
Week 8 - Inflation
https://ejudge.it.kmitl.ac.th/problem/8233
'''


def main():
    '''Main Function'''

    price = int(float(input()) * 100)
    years = int(input())

    for _ in range(years):
        price = price * 10381 // 10000

    print('%d.%02d' % (price//100, price%100))


main()
