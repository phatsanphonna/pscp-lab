'''Week 8 - FourDirections'''




def main():
    '''Main Function'''

    sequence = input()
    sequence_length = len(sequence)

    for i in range(sequence_length):
        if i + 1 == sequence_length:
            print('  *  ')
        else:
            print('  *  ', end=' ')
    
    for index, char in enumerate(sequence):
        if index + 1 == sequence_length:
            if 
