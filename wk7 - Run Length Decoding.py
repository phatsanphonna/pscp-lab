'''Week 7 - Run Length Decoding'''


def main():
    '''Main Function'''

    encoded_message = input()

    counter = ''

    for char in encoded_message:
        if char.isnumeric():
            counter += char
        else:
            print(char * int(counter), end='')
            counter = ''


main()
