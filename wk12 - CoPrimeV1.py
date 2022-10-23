'''
Week 12 - CoPrimeV1
https://ejudge.it.kmitl.ac.th/problem/8336
'''


def main():
    '''Main Function'''

    num_1 = abs(int(input()))
    num_2 = abs(int(input()))

    max_number = max([num_1, num_2])
    gcd_value = 0

    for i in range(1, max_number+1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd_value = i

    if gcd_value == 1:
        print('YES')
    else:
        print('NO')

    print(gcd_value)


main()
