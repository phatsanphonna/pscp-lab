'''
Week 12 - GCD_v1
https://ejudge.it.kmitl.ac.th/problem/8335
'''


def main():
    '''Main Function'''

    num_1 = abs(int(input()))
    num_2 = abs(int(input()))

    min_number = min([num_1, num_2])
    gcd_value = 0

    for i in range(1, min_number+1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd_value = i

    print(gcd_value)


main()
