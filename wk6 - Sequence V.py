'''Week 5 - Sequence V'''


def main():
    '''Main Function'''

    number = int(input())
    increment = 0
    for _ in range(number):
        if number - increment == 1:
            print(number - increment, end='')
            break

        for j in range(7):
            if number - increment <= 0:
                break

            if j == 6:
                print(number - increment, end='\n')
            else:
                if number - increment == 1:
                    print(number - increment, end='')
                else:
                    print(number - increment, end=' ')

            increment += 1


main()
