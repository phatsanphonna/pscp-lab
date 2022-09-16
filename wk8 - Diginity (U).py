'''Week 8 - Diginity'''


def main():
    '''Main Function'''

    number_list = []

    while True:
        number = input()

        if number == '0':
            break

        number_array = [0, 0]

        while len(number_array) > 1:
            for n in number:
                number_array.append(int(n))

            print(number_array)

            total_value = sum(number_array)

            print('Total value: %d' % total_value)

            number_array = [int(i) for i in str(total_value)]

        number_list.append(number_array[0])

    print(*number_list, sep='\n')


main()
