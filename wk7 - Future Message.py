'''Week 6 - Future Message'''


def main():
    '''Main Function'''

    sentence = input()

    if sentence.isdigit() or sentence.isdecimal():
        print('Number')
    elif sentence.isupper():
        print('Uppercase')
    elif sentence.islower():
        print('Lowercase')
    elif sentence.istitle():
        print('Title')
    elif sentence.isspace():
        print('Space')
    else:
        print('Other')


main()
