'''
Week 9 - Saint Seiya
https://ejudge.it.kmitl.ac.th/problem/8266
'''


def main():
    '''Main Function'''

    total_seconds = int(input())
    required_punch = int(input())

    total_punch = 0

    for second in range(2, total_seconds+1, 2):
        if total_punch >= required_punch:
            total_punch += 12 * (total_seconds - second + 1)
            break

        if second % 6 == 0:
            total_punch += 1
        elif second % 2 == 0:
            total_punch += 165

    print(total_punch)


main()
