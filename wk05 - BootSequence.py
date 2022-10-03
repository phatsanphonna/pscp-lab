'''Week 5 - BootSequence'''


def main():
    '''Main Function'''

    number = int(input())

    for i in range(1, number+1):
        if i == number:
            print(i, end='')
            break

        print(i, end='_')


main()
