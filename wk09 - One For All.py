'''
Week 9 - One For All
https://ejudge.it.kmitl.ac.th/problem/8252
'''


def main():
    '''Main Function'''

    loops = int(input())

    for i in range(1, loops+1):
        name = input()

        if i == loops:
            print('%s_%d' % (name, i), end='')
        elif i % 2 == 0:
            print('%s%s' % (name, '-' * i), end='')
        elif i % 2 != 0:
            print('%s%s' % (name, '*' * i), end='')


main()
