'''Week 8 - RuleOfThree'''


def main():
    '''Main Function'''

    total_pieces = int(input())

    best_snack_price = 0
    best_snack_weight = 0

    best_price_per_weight = 0

    for i in range(total_pieces):
        price = float(input())
        weight = float(input())

        price_per_weight = price / weight

        if i == 0:
            best_price_per_weight = price_per_weight
            best_snack_price = price
            best_snack_weight = weight
            continue

        if price_per_weight < best_price_per_weight:
            best_price_per_weight = price_per_weight

            best_snack_price = price
            best_snack_weight = weight
        elif price_per_weight == best_price_per_weight:
            if price < best_snack_price:
                best_price_per_weight = price_per_weight

                best_snack_price = price
                best_snack_weight = weight

    print('%.2f %.2f' % (best_snack_price, best_snack_weight))


main()
