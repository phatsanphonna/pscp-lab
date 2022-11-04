'''Week 15 - Inverter'''


def main():
    '''Main Function'''

    bits = input()

    flip_bits = ''

    for bit in bits:
        if bit == '0':
            flip_bits += '1'
        elif bit == '1':
            flip_bits += '0'

    print(flip_bits.lstrip('0'))


main()
