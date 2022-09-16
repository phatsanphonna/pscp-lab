'''Week 8 - Elo'''


def main():
    '''Main Function'''

    ra_value = int(input())
    rb_value = int(input())

    choice = input()

    if choice == 'A':
        ea_value = 1 / (1 + (10**((rb_value-ra_value) / 400)))
        print('%.2f' % ea_value)
    elif choice == 'B':
        eb_value = 1 / (1 + (10**((ra_value-rb_value) / 400)))
        print('%.2f' % eb_value)


main()
