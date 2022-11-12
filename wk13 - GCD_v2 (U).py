'''
Week 12 - GCD_v2
https://ejudge.it.kmitl.ac.th/problem/8335
'''


def main():
    '''Main Function'''

    num_1 = abs(int(input()))
    num_2 = abs(int(input()))

    for i in range(max(num_1, num_2), 0, -1):
        if num_1 % i == 0 and num_2 % i == 0:
            print(i)
            break


main()
