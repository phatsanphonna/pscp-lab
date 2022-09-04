'''Week 5 - Sequence I'''


def main():
    '''Main Function'''

    number = int(input())

    for _ in range(1, number+1):
        for j in range(1, number+1):
            if j == number:
                print(j, end='\n')
            else:
                print(j, end=' ')


main()
