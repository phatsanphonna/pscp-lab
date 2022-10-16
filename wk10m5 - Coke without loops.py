'''
Midterm 5 - Coke (without loops)
Week 10 - Coke (without loops)
https://ejudge.it.kmitl.ac.th/problem/8273
'''


def main():
    '''Main Function'''

    normal_price = int(input())
    promo_caps = int(input())
    promo_price = int(input())
    get_at_least = int(input())

    if promo_caps == 0:
        print(normal_price * get_at_least)
        return

    promo_bottle, fraction = divmod(get_at_least - 1, promo_caps)
    normal_bottle = get_at_least - promo_bottle

    total_price = normal_bottle * normal_price + promo_price * promo_bottle
    total_price += normal_bottle

    # print(normal_bottle, discount_bottle)
    print(total_price)


main()
