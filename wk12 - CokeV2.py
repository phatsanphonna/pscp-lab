'''
Midterm 5 - Coke (without loops)
Week 10 - Coke (without loops)
Week 12 - CokeV2
https://ejudge.it.kmitl.ac.th/problem/8340
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

    if get_at_least == 0:
        print(0)
        return

    promo_sequence = (normal_price * (promo_caps - 1) + promo_price)

    promo_bottle, fraction = divmod(get_at_least - 1, promo_caps)

    total_pay = promo_sequence * promo_bottle
    total_pay += (fraction + 1) * normal_price

    print(total_pay)


main()
