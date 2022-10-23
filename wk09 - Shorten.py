'''Week 9 - Shorten'''


def main():
    '''Main Function'''

    first_number = 0
    last_number = 0

    is_refresh = True

    string_builder = ''

    while True:
        number = int(input())

        if is_refresh:
            first_number = number
            is_refresh = False
            continue

        if number == -1:
            break

        if abs(first_number - last_number) == 1:
            last_number = number
        else:
            string_builder += '%d-%d ' % (first_number, last_number)
            first_number = 0
            last_number = 0

    print(string_builder)


main()
