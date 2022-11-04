'''Week 12 - All_Primes'''


def find_prime(number: int):
    '''Find Prime'''

    if number <= 1:
        return 0

    fully_mod_value = []

    for i in range(1, number+1):
        if number % i == 0:
            fully_mod_value.append(i)

        if len(fully_mod_value) > 2:
            return 0

    if len(fully_mod_value) > 2:
        return 0
    else:
        return 1


def main():
    '''Main Function'''

    number = int(input())
    total_prime = 0

    for i in range(1, number+1):
        total_prime += find_prime(i)

    print(total_prime)


main()
