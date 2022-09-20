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
            continue

        while len(number) != 1:
            total = 0

            for num in number:
                total += int(num)

            number = str(total)

        number_list.append(number)

    for number in number_list:
        print(number)


main()
