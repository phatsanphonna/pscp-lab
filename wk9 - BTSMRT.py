'''Week 9 - BTSMRT'''


def main():
    '''Main Function'''

    day = input()
    age = float(input())
    height = float(input())

    if age < 14 and height < 90:
        print('FREE')
        return

    if day == 'Senior Day':
        if age >= 60:
            print('FREE')
        else:
            print('PAY')
    elif day == 'Children Day':
        if age < 14 and height <= 140:
            print('FREE')
        else:
            print('PAY')
    elif day == 'Normal Day':
        print('PAY')


main()
