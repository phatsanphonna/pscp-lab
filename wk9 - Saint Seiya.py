'''Week 9 - Saint Seiya'''


def check_ryu_sei_ken(second: int):
    '''Check that this second is valid for Pegasasu Ryu Sei Ken'''

    return second % 2 == 0


def check_sui_sei_ken(second: int):
    '''Check that this second is valid for Pegasasu Sui Sei Ken'''

    return second % 6 == 0


def main():
    '''Main Function'''

    total_seconds = int(input())
    required_punch = int(input())

    total_punch = 0

    rolling_crash_activate = False

    for i in range(1, total_seconds+1):
        if rolling_crash_activate:
            total_punch += 12
            continue

        if total_punch >= required_punch:
            rolling_crash_activate = True
            continue

        if check_sui_sei_ken(i):
            total_punch += 1
        elif check_ryu_sei_ken(i):
            total_punch += 165

        print(
            f'second: {i}, total punch: {total_punch}, rolling crash activate: {rolling_crash_activate}')

    print(total_punch)


main()
