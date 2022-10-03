'''
Week 8 - Inflation
https://ejudge.it.kmitl.ac.th/problem/8233
'''


INFLATION_RATE = 0.0381


def main():
    '''Main Function'''

    price = float(input())
    years = int(input())

    inflation = float('%.4f' % (1 + INFLATION_RATE)**years)
    price_with_inflation = inflation * price
    price_with_inflation = int(price_with_inflation * 100) / 100

    print('%.2f' % price_with_inflation)


main()
