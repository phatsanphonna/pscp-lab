'''Week 5 - SumOfNumber'''


def main():
    """Loop and print ans"""

    req = int(input())

    sum_num = 0

    while True:
        num = int(input())
        if num == -1:
            break
        else:
            sum_num += num
            if sum_num == req:
                break

    print(sum_num)


main()
