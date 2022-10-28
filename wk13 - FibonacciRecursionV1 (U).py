'''
Week 13 - FibonacciRecursionV1
https://ejudge.it.kmitl.ac.th/problem/8342
'''


def main():
    '''Main Function'''

    n_value = int(input())

    total = 0
    a_value = 0
    b_value = 1

    def increment(value: int):
        '''Increment value'''

        nonlocal total, n_value, a_value, b_value

        if value > n_value:
            return

        print('value', a_value, b_value)

        total += a_value + b_value
        a_value = b_value
        b_value = total

        increment(value + 1)

    increment(2)

    print(total)


main()
