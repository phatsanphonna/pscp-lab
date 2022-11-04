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

    for i in range(2, number):
        if number % i == 0:
            print('NO')
            return

    print('YES')


main()
