'''
Week 13 - FibonacciRecursionV1
https://ejudge.it.kmitl.ac.th/problem/8342
'''


def find_fibonacci(value: int):
    '''Find Fibonacci'''

    if value <= 0:
        return abs(value)

    return find_fibonacci(value - 1) + find_fibonacci(value - 2)


def main():
    '''Main Function'''

    n_value = int(input())

    total = find_fibonacci(n_value)

    print(total)


main()
