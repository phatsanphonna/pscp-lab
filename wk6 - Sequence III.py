'''Week 5 - Sequence III'''


def main():
    '''Main Function'''

    number = int(input())

    for i in range(2, number+2):
        for j in range(i, number+i):
            if j == number+i:
                print(j, end='\n')
                continue

            print(j, end=' ')

        print()

main()
