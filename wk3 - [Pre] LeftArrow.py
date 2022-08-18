'''Week 3 - [Pre] LeftArrow.py'''


def main():
    '''Main Function'''

    light_width = int(input())
    light_height = int(input())

    gap = int((light_height - 1) / 2)

    for i in range(gap):
        print(' '*(gap - i) + '*'*light_width)

    print('*' * light_width)

    for i in range(gap, 0, -1):
        print(' '*(gap - i + 1) + '*'*light_width)


main()
