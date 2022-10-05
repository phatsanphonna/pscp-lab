'''
Week 8 - Harshad
https://ejudge.it.kmitl.ac.th/problem/8245
'''


def main():
    '''Main Function'''

    for _ in range(10):
        number = abs(int(input()))

        divide_number = 0

        if number == 0:
            print('No')
            continue

        for num in str(number):
            divide_number += int(num)

        if number % divide_number == 0:
            print('Yes')
        else:
            print('No')


main()
