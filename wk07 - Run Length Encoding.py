'''Week 7 - Run Length Encoding'''


def main():
    '''Main Function'''

    message = input()

    encoded_message = ''

    checker = message[0]
    counter = 0

    for index, char in enumerate(message):
        if char == checker:
            counter += 1
        else:
            encoded_message += str(counter) + checker
            checker = message[index]
            counter = 1

    encoded_message += str(counter) + checker

    print(encoded_message)


main()
