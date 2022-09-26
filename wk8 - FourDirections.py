'''Week 8 - FourDirections'''


def print_upper_and_bottom(sequence_length: int):
    '''Print upper and bottom of arrows'''

    for i in range(sequence_length):
        if i + 1 == sequence_length:
            print('  *  ')
        else:
            print('  *  ', end=' ')


def print_second_line(char: str, end: bool=True):
    '''Print the second line to the screen'''

    if end:
        if char == 'U':
            print(' *** ', end=' ')
        elif char == 'D':
            print('  *  ', end=' ')
        elif char == 'L':
            print(' *   ', end=' ')
        elif char == 'R':
            print('   * ', end=' ')
    else:
        if char == 'U':
            print(' *** ')
        elif char == 'D':
            print('  *  ')
        elif char == 'L':
            print(' *   ')
        elif char == 'R':
            print('   * ')


def print_third_line(char: str, end: bool=True):
    '''Print the third line to the screen'''

    if end:
        if char in 'UD':
            print('* * *', end=' ')
        elif char in 'LR':
            print('*****', end=' ')
    else:
        if char in 'UD':
            print('* * *')
        elif char in 'LR':
            print('*****')


def print_forth_line(char: str, end: bool=True):
    '''Print the forth line to the screen'''

    if end:
        if char == 'U':
            print('  *  ', end=' ')
        elif char == 'D':
            print(' *** ', end=' ')
        elif char == 'L':
            print(' *   ', end=' ')
        elif char == 'R':
            print('   * ', end=' ')
    else:
        if char == 'U':
            print('  *  ')
        elif char == 'D':
            print(' *** ')
        elif char == 'L':
            print(' *   ')
        elif char == 'R':
            print('   * ')


def main():
    '''Main Function'''

    sequence = input()
    sequence_length = len(sequence)

    print_upper_and_bottom(sequence_length)

    for index, char in enumerate(sequence):
        if index + 1 == sequence_length:
            print_second_line(char, end=False)
        else:
            print_second_line(char)

    for index, char in enumerate(sequence):
        if index + 1 == sequence_length:
            print_third_line(char, end=False)
        else:
            print_third_line(char)

    for index, char in enumerate(sequence):
        if index + 1 == sequence_length:
            print_forth_line(char, end=False)
        else:
            print_forth_line(char)

    print_upper_and_bottom(sequence_length)


main()