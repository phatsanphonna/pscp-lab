'''
[Recommend]
Week 5 - Donut
'''


def main():
    '''Main Function'''

    a_val = int(input())
    b_val = int(input())
    c_val = int(input())
    d_val = int(input())

    total_promo_donuts = b_val + c_val
    price_per_box = a_val * b_val
    total_box = d_val // total_promo_donuts

    remain_to_buy = d_val - (total_box * total_promo_donuts)

    if remain_to_buy >= b_val:
        total_box += 1
        remain = 0

    price = total_box * price_per_box + remain * a_val
    piece = total_box * total_promo_donuts + remain_to_buy

    print(price, piece)


main()
