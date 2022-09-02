'''Week 5 - Triangle I'''


def main():
    '''Main Function'''

    a_value = float(input())**2
    b_value = float(input())**2
    c_value = float(input())**2

    combine_a_b_value = a_value + b_value

    if abs(c_value - combine_a_b_value) <= 0.01:
        print('Yes')
        return
        
    if c_value - combine_a_b_value <= 0.01:
        print('Yes')
    else:
        print('No')


main()
