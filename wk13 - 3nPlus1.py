'''
Week 13 - 3nPlus1
https://ejudge.it.kmitl.ac.th/problem/8351
'''


def main():
    '''Main Function'''

    increment_list = []

    while True:
        value = int(input())

        if value == 0:
            break

        increment = 1

        while not value == 1:
            if value % 2 == 0:
                value /= 2
            else:
                value = value * 3 + 1

            increment += 1

        increment_list.append(increment)

    print(*increment_list, sep='\n')


main()
