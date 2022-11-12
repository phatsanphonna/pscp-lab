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

    for i in range(2, number):
        if number % i == 0:
            print('No')
            return

    print('Yes')


main()
