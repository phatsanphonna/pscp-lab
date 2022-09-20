'''
[Recommend]
Week 8 - Ball
'''


def main():
    '''Main Function'''

    height = float(input())

    count = 0

    while True:
        height = height * 0.6

        if height < 0.01:
            break

        count += 1

    print(count)


main()
