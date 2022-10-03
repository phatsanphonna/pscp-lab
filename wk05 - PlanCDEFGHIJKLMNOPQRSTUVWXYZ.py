'''Week 5 - PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''


def descend(num1: float, num2: float, num3: float):
    '''Descend'''

    first_number = num1
    second_number = 0
    third_number = 0

    if num2 > first_number:
        first_number = num2
    if num3 > first_number:
        first_number = num3

    if first_number == num1:
        second_number = num2

        if num3 > second_number:
            second_number = num3
            third_number = num2
        else:
            second_number = num2
            third_number = num3
    elif first_number == num2:
        second_number = num1

        if num3 > second_number:
            second_number = num3
            third_number = num1
        else:
            second_number = num1
            third_number = num3
    elif first_number == num3:
        second_number = num1

        if num2 > second_number:
            second_number = num2
            third_number = num1
        else:
            second_number = num1
            third_number = num2

    first_number = '%.2f' % first_number
    second_number = '%.2f' % second_number
    third_number = '%.2f' % third_number

    return first_number, second_number, third_number


def ascend(num1: float, num2: float, num3: float):
    '''Ascend'''

    first_number = num1
    second_number = 0
    third_number = 0

    if num2 < first_number:
        first_number = num2
    if num3 < first_number:
        first_number = num3

    if first_number == num1:
        second_number = num2

        if num3 < second_number:
            second_number = num3
            third_number = num2
        else:
            second_number = num2
            third_number = num3
    elif first_number == num2:
        second_number = num1

        if num3 < second_number:
            second_number = num3
            third_number = num1
        else:
            second_number = num1
            third_number = num3
    elif first_number == num3:
        second_number = num1

        if num2 < second_number:
            second_number = num2
            third_number = num1
        else:
            second_number = num1
            third_number = num2

    first_number = '%.2f' % first_number
    second_number = '%.2f' % second_number
    third_number = '%.2f' % third_number

    return first_number, second_number, third_number


def main():
    '''Main Function'''

    asc_or_dsec = input().lower()

    number1 = float(input())
    number2 = float(input())
    number3 = float(input())

    if asc_or_dsec == 'ascend':
        first_number, second_number, third_number = ascend(
            number1, number2, number3)
    elif asc_or_dsec == 'descend':
        first_number, second_number, third_number = descend(
            number1, number2, number3)

    print(first_number, second_number, third_number, sep=', ')


main()
