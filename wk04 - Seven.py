'''Week 4 - Seven'''


def find_last_digit(number: int):
    '''Find last digit'''

    mod_value = number % 4

    if mod_value == 1:
        print(7)
    elif mod_value == 2:
        print(9)
    elif mod_value == 3:
        print(3)
    elif mod_value == 0:
        print(1)


def main():
    '''Main Function'''

    number = int(input())

    find_last_digit(number)


main()
