'''Week 4 - Seven'''


def find_last_digit(number: int):
    '''Find last digit'''

    mod_value = number // 7

    last_digit = int(str(mod_value)[-1])

    if last_digit == 1:
        print(7)
    elif last_digit == 7:
        print(9)
    elif last_digit == 9:
        print(3)
    elif last_digit == 3:
        print(1)


def main():
    '''Main Function'''

    number = int(input())

    find_last_digit(number)


main()
