'''
Midterm 4 - Calculator
Week 10 - Calculator (Less Loops)
https://ejudge.it.kmitl.ac.th/problem/8271
'''


def main():
    '''Main Function'''

    n_value = input()
    n_value_length = len(n_value)

    total_press = 0

    if n_value == '1':
        print(1)
        return

    if len(n_value) < 2:
        print(int(n_value) * 2)
        return

    total_press = 9 * 2

    for i in range(2, n_value_length+2):
        decrement = int('9'*(i-1)) - 10 * (i-1)

        multiplier = int(n_value) - decrement

        print(decrement, multiplier, n_value)

        total_press += multiplier * (i + 1 + 1)

        print('total press', total_press)

    print(total_press)


main()
