'''
Midterm 4 - Calculator
Week 10 - Calculator (Less Loops)
https://ejudge.it.kmitl.ac.th/problem/8271
'''


def calculate_max_number(length: int):
    '''Calculate Max Number'''

    if length == 1:
        return 9

    return int('8' + '9' * (length-1))

def main():
    '''Main Function'''

    n_value = input()
    n_value_length = len(n_value)

    if n_value == '1':
        print(1)
        return
    
    if n_value_length == 1:
        print(2 * int(n_value))
        return

    total_press = 18

    for i in range(2, n_value_length+1):
        if i == n_value_length:
            press = abs(10**(i) - int(n_value))
        else:
            press = calculate_max_number(i)
        
        print(press, i + 1, 10**i)

        total_press += press * (i + 1)

    print(total_press)

main()
