'''
Week 11 - Tuple's Sad life
https://ejudge.it.kmitl.ac.th/problem/8277
'''


def main():
    '''Main Function'''

    sequence = tuple(input().rstrip().split(' '))
    char = input()

    char_first_pos = sequence.index(char)
    char_count = sequence.count(char)

    for _ in range(char_count):
        for _ in range(char_count):
            print(char_first_pos, end=' ')

        print()


main()
