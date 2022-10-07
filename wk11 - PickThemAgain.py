'''
Week 11 - PickThemAgain
https://ejudge.it.kmitl.ac.th/problem/8284
'''


def main():
    '''Main Function'''

    sequence = input().split(' ')
    sequence = [int(i) for i in sequence]

    number_list = []

    for number in sequence:
        if number % 3 == 0 or number % 5 == 0:
            number_list.append(number)

    if not number_list:
        print('Nope')
        return

    print(*reversed(number_list), sep='\n')


main()
