'''
Midterm 5 - Coke
Week 10 - Coke
https://ejudge.it.kmitl.ac.th/problem/8273
'''


def main():
    '''Main Function'''

    normal_price = int(input())
    promo_caps = int(input())
    promo_price = int(input())
    get_at_least = int(input())

    total_price = 0

    if promo_caps == 0:
        print(normal_price * get_at_least)
        return

    for i in range(get_at_least):
        if i != 0 and i % promo_caps == 0:
            total_price += promo_price
            continue

        total_price += normal_price

    print(total_price)


main()
