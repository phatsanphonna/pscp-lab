'''Week 5 - WeightStation'''


def main():
    '''Main Function'''

    avg_weight = float(input())

    pos1_weight = float(input())
    pos2_weight = float(input())
    pos3_weight = float(input())
    pos4_weight_broken = avg_weight * 4 \
        - pos1_weight - pos2_weight - pos3_weight

    total_weight = pos1_weight + pos2_weight + pos3_weight + pos4_weight_broken

    is_overweight = False
    is_unbalance = False

    if total_weight > 15000:
        is_overweight = True

    if pos1_weight / avg_weight > 1.5 or pos1_weight / avg_weight < 0.5:
        is_unbalance = True

    if pos2_weight / avg_weight > 1.5 or pos2_weight / avg_weight < 0.5:
        is_unbalance = True

    if pos3_weight / avg_weight > 1.5 or pos3_weight / avg_weight < 0.5:
        is_unbalance = True

    if pos4_weight_broken / avg_weight > 1.5 \
            or pos4_weight_broken / avg_weight < 0.5:
        is_unbalance = True

    if is_overweight and is_unbalance:
        print('Overweight')
        return

    if is_overweight:
        print('Overweight')
        return

    if is_unbalance:
        print('Unbalance')
        return

    print('Pass %.2f' % pos4_weight_broken)


main()
