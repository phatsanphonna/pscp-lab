'''Week 5 - Day I'''


def main():
    '''Main Function'''

    year = int(input())

    if year % 4 == 0:
        if year % 400 == 0:
            print('Yes')
        elif year % 100 == 0:
            print('No')
        else:
            print('Yes')
    else:
        print('No')


main()
