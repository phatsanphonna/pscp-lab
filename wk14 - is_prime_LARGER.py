'''Week 14 - is_prime_LARGER'''


def main():
    '''Main Function'''

    number = int(input())

    if number <= 1:
        print('False')
        return

    for i in range(2, int(number**0.5)+1, 3):
        if number % i == 0:
            print('False')
            return

    print('True')


main()
