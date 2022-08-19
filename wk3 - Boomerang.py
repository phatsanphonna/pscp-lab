'''Week 3 - Boomerang'''


def function_1(x_value: int):
    '''Function 1'''

    return x_value + 1


def function_2(y_value: int):
    '''Function 2'''

    return (7 * (y_value**3)) + (2 * (y_value**2)) - (31 * y_value) + 1


def function_3(z_value: int):
    '''Function 3'''

    return -1 * z_value


def function_4(x_value: int, y_value: int):
    '''Function 4'''

    return (x_value + y_value) * (x_value - y_value)


def function_5(x_value: int, y_value: int, z_value: int):
    '''Function 5'''

    return (y_value - ((y_value**2) - (4*x_value*z_value))**0.5) / (2 * x_value)


def main():
    '''Main Function'''

    value_x = int(input())
    value_y = int(input())
    value_z = int(input())

    print(function_1(value_x))
    print(function_2(value_y))
    print(function_3(value_z))
    print(function_4(value_x, value_y))
    print(function_5(value_x, value_y, value_z))


main()
