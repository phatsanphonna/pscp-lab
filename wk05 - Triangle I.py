'''Week 5 - Triangle I'''


def find_mx_3(num1: int, num2: int, num3: int):
    '''Find mximum value of five value'''

    final_value = num1

    if not final_value > num1:
        final_value = num1
    if not final_value > num2:
        final_value = num2
    if not final_value > num3:
        final_value = num3

    return final_value


def find_mx_2(num1: int, num2: int):
    '''Find mximum value of five value'''

    if num1 > num2:
        return num1, num2
    elif num1 > num2:
        return num2, num1
    else:
        return num1, num2

def main():
    '''Main Function'''

    a_value = float(input())
    b_value = float(input())
    c_value = float(input())

    num1 = find_mx_3(a_value, b_value, c_value)
    num2 = 0
    num3 = 0

    if num1 == a_value:
        num2, num3 = find_mx_2(b_value, c_value)
    elif num1 == b_value:
        num2, num3 = find_mx_2(a_value, c_value)
    elif num1 == c_value:
        num2, num3 = find_mx_2(a_value, b_value)

    combine_a_b_value = (num2**2 + num3**2)**0.5

    if abs(num1 - combine_a_b_value) <= 0.01:
        print('Yes')
    else:
        print('No')


main()
