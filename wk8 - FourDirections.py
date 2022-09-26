'''Week 8 - FourDirections'''


def second_line(char: str):
    '''Print second line out to screen'''

    if char == 'U':
        print(' *** ')

def main():
    '''Main Function'''

    sequence = input()
    sequence_length = len(sequence)

    for index in range(sequence_length):
        if index + 1 == sequence_length:
            print('  *  ')
        else:
            print('  *  ', end=' ')
    
    for index, char in enumerate(sequence):
        if index + 1 == sequence_length:
            print('  *  ')
        else:
            print('  *  ', end=' ')
        
