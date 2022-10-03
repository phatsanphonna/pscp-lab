'''
[Recommend]
Week 5 - Donut
'''


def main():
    '''Main Function'''

    donut_price = int(input())
    promotion_amount = int(input())
    extra_donut_amount = int(input())
    want_to_buy = int(input())

    promo_donuts = promotion_amount + extra_donut_amount
    price_per_promo = donut_price * promotion_amount
    total_promo = want_to_buy // promo_donuts

    remain_to_buy = want_to_buy - (total_promo * promo_donuts)

    if remain_to_buy >= promotion_amount:
        total_promo += 1
        remain_to_buy = 0

    price = (total_promo * price_per_promo) + (remain_to_buy * donut_price)
    piece = (total_promo * promo_donuts) + remain_to_buy

    print(price, piece)


main()
