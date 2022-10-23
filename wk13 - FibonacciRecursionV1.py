'''
Week 13 - FibonacciRecursionV1
https://ejudge.it.kmitl.ac.th/problem/8342
'''


def main():
    '''Main Function'''

    total = 0

    def increment(value: int):
        '''Increment value'''

        nonlocal total

        if value == 0:
            return

        total += value

        increment(value - 1)

    n_value = int(input())

    increment(n_value)

    print(total)


main()
