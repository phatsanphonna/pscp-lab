'''Week 8 - Inflation'''


INFLATION_RATE = 0.0381


def main():
    '''Main Function'''

    price = float(input())
    years = int(input())

    price_with_inflation = price * (1 + INFLATION_RATE*years)

    price_with_inflation = int(price_with_inflation * 100) / 100

    print('%.2f' % price_with_inflation)


main()
