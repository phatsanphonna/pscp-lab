'''Week 8 - Milk'''


def main():
    '''Main Function'''

    price_per_bottle = int(input())
    promotion = int(input())
    exchange_promotion = int(input())
    customer_money = int(input())

    total_bottles = customer_money // price_per_bottle

    total_promotion_bottles = (total_bottles // promotion) * exchange_promotion

    total_bottles += total_promotion_bottles

    print(total_bottles)


main()
