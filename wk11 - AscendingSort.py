'''
Week 11 - AscendingSort
https://ejudge.it.kmitl.ac.th/problem/8282
'''


def main():
    '''Main Function'''

    number_list = []

    for _ in range(5):
        number_list.append(int(input()))

    print(*sorted(number_list), sep='\n')


main()
