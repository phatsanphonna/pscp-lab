'''
Week 13 - Divide3Or5
https://ejudge.it.kmitl.ac.th/problem/8346
'''


def main():
    '''Main Function'''

    number = int(input())

    total = 0

    for i in range(1, number+1):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    print(total)


main()
