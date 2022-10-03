'''
[Recommend]
Week 7 - FOR!F-Ball
'''


def find_action(action: str):
    '''Find which action it is. A, B or C'''

    if action == 'A':
        return 1
    if action == 'B':
        return 2
    if action == 'C':
        return 3


def main():
    '''Main Function'''

    sequences = input()

    # 1 = left, 2 = middle, 3 = right
    position = 1

    for action in sequences:
        sequence = find_action(action)

        if sequence == 1:
            if position == 1:
                position = 2
            elif position == 2:
                position = 1

        elif sequence == 2:
            if position == 2:
                position = 3
            elif position == 3:
                position = 2

        elif sequence == 3:
            if position == 1:
                position = 3
            elif position == 3:
                position = 1

    print(position)


main()
