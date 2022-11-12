'''Week 15 - Heads and Legs'''

# x + y = a
# 4x + 2y = b


def main():
    '''Main Function'''

    total_pet = int(input())
    total_leg = int(input())

    y_value = (total_leg - (4 * total_pet)) / -2
    x_value = total_pet - y_value

    if y_value < 0 or x_value < 0:
        print('Impossible')
        return

    if x_value - int(x_value) != 0 or y_value - int(y_value) != 0:
        print('Impossible')
        return

    print(int(x_value), int(y_value))


main()
