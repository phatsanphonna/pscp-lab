'''Week 5 - Sequence II'''


def main():
    '''Main Function'''

    number = int(input())

    for i in range(1, number+1):
        if i == number:
            print(i**2, end='')
        else:
            print(i**2, end=' ')


main()
