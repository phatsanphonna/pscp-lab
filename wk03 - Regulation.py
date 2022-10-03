'''Week 3 - Regulation'''


def main():
    '''Main Function'''

    value_1 = input()
    value_2 = float(input())
    value_3 = input()

    print(' '*(30 - len(value_1)) + value_1)
    print('0'*(30 - len(value_1)) + value_1)
    print('%.2f' % round(value_2, 2))
    print('%.12f' % round(value_2, 12))
    print(' '*(40 - len(value_3)) + value_3)

main()
