'''Week 5 - LargestNumber'''


def find_highest_num(num1, num2, num3, num4, num5):
    '''Find the highest number'''

    highest_num = num1

    if num2 > highest_num:
        highest_num = num2
    if num3 > highest_num:
        highest_num = num3
    if num4 > highest_num:
        highest_num = num4
    if num5 > highest_num:
        highest_num = num5

    return highest_num


def main():
    '''Main Function'''

    num1 = input()
    num2 = input()
    num3 = input()

    comb1 = num1 + num2 + num3
    comb2 = num1 + num3 + num2
    comb3 = num2 + num1 + num3
    comb4 = num2 + num3 + num1
    comb5 = num3 + num1 + num2
    comb6 = num3 + num2 + num1

    highest_number = find_highest_num(comb1, comb2, comb3, comb4, comb5)

    if comb6 > highest_number:
        highest_number = comb6

    print(int(highest_number))


main()
