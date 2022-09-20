'''
<Recommend>
Week 7 - Virus 1
'''


def main():
    '''Main Function'''

    virus = input()

    count = 0

    for character in virus:
        if character == "o":
            count += 1

    print(count)


main()
