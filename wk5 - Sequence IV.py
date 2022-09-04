'''Week 5 - Sequence IV'''


def main():
    '''Main Function'''

    number = int(input())

    for i in range(number):
        increment = i*number

        for j in range(1, number+1):
            # print('j range', j, number+1)
            if j + increment == number * (i + 1):
                print(j + increment, end='\n')
            else:
                print(j + increment, end=' ')


main()
