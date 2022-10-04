'''
Midterm 2 - Parity
Week 10 - Parity
https://ejudge.it.kmitl.ac.th/problem/8270
'''


def is_even(bit_count: int):
    '''Parameter is even or not even'''

    return bit_count % 2 == 0


def main():
    '''Main Function'''

    bits = input()
    odd_or_even = input()

    bit_count = 0

    for bit in bits:
        if bit == '1':
            bit_count += 1

    if odd_or_even == 'Even' and not is_even(bit_count):
        bits += '1'
    elif odd_or_even == 'Even' and is_even(bit_count):
        bits += '0'
    elif odd_or_even == 'Odd' and not is_even(bit_count):
        bits += '0'
    elif odd_or_even == 'Odd' and is_even(bit_count):
        bits += '1'

    print(bits)


main()
