'''
[Recommend]
Week 8 - Milk (U)
https://ejudge.it.kmitl.ac.th/problem/8238
- โดน Timeout
'''


def main():
    '''Main Function'''

    price_per_bottle = int(input())
    promotion = int(input())
    exchange_promotion = int(input())
    customer_money = int(input())

    total_bottles = customer_money // price_per_bottle
    total_caps = total_bottles

    if promotion == 0:
        print(total_bottles)
        return

    total_promotion_bottles = 0

    while total_caps >= promotion:
        promotion_bottles, caps_left = divmod(total_bottles, promotion)

        total_promotion_bottles += promotion_bottles * exchange_promotion

        total_bottles += promotion_bottles
        total_caps = promotion_bottles + caps_left

    print(total_bottles)


main()
