'''Week 5 - Sequence VII'''


def main():
    '''Main Function'''

    number = int(input())

    for i in range(1, number+1):
        for j in range(1, i+1):
            if j == i:
                print(j, end='\n')
            else:
                print(j, end=' ')

    for i in reversed(range(1, number)):
        for j in range(1, i+1):
            if j == i:
                print(j, end='\n')
            else:
                print(j, end=' ')


main()
