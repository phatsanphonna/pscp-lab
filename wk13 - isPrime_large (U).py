'''
Week 12 - isPrime_large
https://ejudge.it.kmitl.ac.th/problem/8357
'''


def main():
    '''Main Function'''

    number = int(input())

    if number <= 1:
        print('NO')
        return

    fully_mod_value = []

    for i in range(1, number+1):
        if number % i == 0:
            fully_mod_value.append(i)

            if len(fully_mod_value) > 2:
                print('NO')
                return

    if len(fully_mod_value) > 2:
        print('NO')
    else:
        print('YES')


main()
