'''
Week 13 - Binary
https://ejudge.it.kmitl.ac.th/problem/8344
'''


def main():
    '''Main Function'''

    initial_number = int(input())
    number = initial_number
    bits = ''

    if number < 2:
        print(number)
        return

    while number != 0:
        number, bit = divmod(number, 2)
        bits += str(bit)

    print(*reversed(bits), sep='')


main()
