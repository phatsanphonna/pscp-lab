'''
[Recommend]
Week 9 - PhoneNumber
https://ejudge.it.kmitl.ac.th/problem/8250
'''


def main():
    '''Main Function'''

    phone_number = input()
    dos_or_intl = input()

    if dos_or_intl == 'Domestic':
        if len(phone_number) == 9:
            print(phone_number[0], phone_number[1:5], phone_number[5:])
        elif len(phone_number) == 10:
            print(phone_number[0:2], phone_number[2:6], phone_number[6:])

    elif dos_or_intl == 'International':
        if len(phone_number) == 9:
            print('+66 %s %s' % (phone_number[1:5], phone_number[5:]))
        elif len(phone_number) == 10:
            print('+66%s %s %s' %
                  (phone_number[1], phone_number[2:6], phone_number[6:]))


main()
