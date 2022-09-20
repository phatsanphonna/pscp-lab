'''
[Recommend]
Week 8 - Diginity
'''


def main():
    '''Main Function'''

    number_list = []

    looping = True

    while looping:
        number = input()

        if int(number) == 0:
            looping = False

        while int(number) < 10:
            total = 0

            for n in str(number):
                total += int(n)

            number = total

        number_list.append(number)


    print(*number_list, sep='\n')


main()
