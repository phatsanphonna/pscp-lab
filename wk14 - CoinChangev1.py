'''
Week 14 - CoinChangev1
https://ejudge.it.kmitl.ac.th/problem/8378
'''


def main():
    '''Main Function'''

    money = int(input())

    _25coin, coin_left = divmod(money, 25)
    _10coin, coin_left = divmod(coin_left, 10)
    _5coin, _1coin = divmod(coin_left, 5)

    print(_25coin + _10coin + _5coin + _1coin)


main()
