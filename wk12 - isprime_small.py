'''
Week 12 - isprime_small
https://ejudge.it.kmitl.ac.th/problem/8333
'''


def main():
    '''Main Function'''

    number = int(input())

    if number <= 1:
        print('No')
        return

    fully_mod_value = []

    for i in range(1, number+1):
        if number % i == 0:
            fully_mod_value.append(i)

    if len(fully_mod_value) > 2:
        print('No')
    else:
        print('Yes')


main()
